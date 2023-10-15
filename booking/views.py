# Assistance from CI - Boutique Ado walkthrough
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)

from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .models import Booking, BookingItem
from .forms import BookingForm
from basket.contexts import basket_contents
from tours.models import Tours

import stripe
import json


@require_POST
def cache_booking_data(request):
    """
    A view to capture the save_info information
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment could not be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def booking(request):
    """
    A view to allow the user to create a booking
    """
    # Assistance from CI - Boutique Ado walkthrough
    # Assign stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Handle payment submission
    if request.method == 'POST':
        # Get the session basket
        basket = request.session.get('basket', {})

        # Add the form data to a dictionary
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile_number': request.POST['mobile_number'],
        }

        # Assign the BookingForm with form data to booking_form
        booking_form = BookingForm(form_data)

        # Check if it is valid
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            booking.stripe_pid = pid
            booking.original_basket = json.dumps(basket)
            booking.save()

            # Iterate through line items
            for item_id, item_data in basket.items():
                try:
                    # Get the experience by id
                    experience = Tours.objects.get(id=item_id)

                    # Check if the item_data is a dictionary
                    if isinstance(item_data, dict):
                        number_of_attendees = (
                            item_data['number_of_attendees'])
                        booking_time_slot = (
                            item_data['booking_time_slot'])
                        booking_date = item_data['booking_date']
                        booking_line_item = BookingItem(
                            booking=booking,
                            tour=experience,
                            number_of_attendees=number_of_attendees,
                            booking_date=booking_date,
                            booking_time_slot=booking_time_slot,
                        )
                        booking_line_item.save()
                
                # Raise error if experience does not exist
                except Tours.DoesNotExist:
                    messages.error(request, 'One of the Experiences \
                        in your basket, was not found in our \
                        database. Please contact us for assistance')

                    # Delete the empty order
                    booking.delete()

                    # redirect to the basket view
                    return redirect(reverse('view_basket'))

            # Check if the save info exists in the session
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('booking_success', args=[booking.booking_number])) 
   
        # Raise error is form is invalid
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your info.')
    else:
        # Get the session basket
        basket = request.session.get('basket', {})

        # If not items are present, return error and return to tours
        if not basket:
            messages.error(request, 'No Experiences are currently \
                        in your basket')
            return redirect(reverse('tours'))

        # Assistance from CI - Boutique Ado walkthrough
        # Assign existing basket contents to current_basket
        current_basket = basket_contents(request)

        # Assistance from CI - Boutique Ado walkthrough
        # Get the total key out of the current_basket
        total = current_basket['grand_total']

        # Assistance from CI - Boutique Ado walkthrough
        # Assign grand_total to stripe_total
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Create an empty booking form
        booking_form = BookingForm()

    # Assistance from CI - Boutique Ado walkthrough
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is \
            missing. Did you forget to set it in your \
            environment?')

    # Assign a template
    template = 'booking/booking.html/'

    # Assitance from CI - Boutique Ado walkthrough
    # Assign the context
    context = {
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # Return the rendered view
    return render(request, template, context)

def booking_success(request, booking_number):
    """
    Returns a booking successful view
    """
    # Get the save info from the session
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Booking complete! Your \
        booking number is {booking_number}. A confirmation \
        email has been sent to {booking.email}')

    # Delete basket from the session
    if 'basket' in request.session:
        del request.session['basket']

    # Assign the template variable
    template = 'booking/booking_success.html/'

    # Assign the context variable
    context = {
        'booking': booking,
    }

    # Render the template
    return render(request, template, context)
