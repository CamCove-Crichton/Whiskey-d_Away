from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .contexts import basket_contents
from booking.forms import BookingItemForm
from tours.models import Tours


# Assistance from CI - Boutique Ado walkthrough
def view_basket(request):
    """
    A view to render the contents of the basket with existing data from the
    submitted form, and allow inputs to be edited from the basket
    """
    # Assign existing basket context to basket items
    basket_context = basket_contents(request)
    basket_items = basket_context['basket_items']

    # Create empty forms list to append to
    forms = []

    # Assistance from ChatGPT with delcaring the existing data outside the loop
    # So that when there are no items in the basket there are no errors
    # Initialize existing_data outside the loop
    existing_data = {
        'number_of_attendees_values': [],
    }

    # Iterate through basket items
    for item in basket_items:
        # Get existing data for the current item
        existing_data.update({
            'number_of_attendees': item['number_of_attendees'],
            'booking_date': item['booking_date'],
            'booking_time_slot': item['booking_time_slot'],
            'experience': item['experience'],
            'max_attendees': item['experience'].max_attendees,
        })

        # Create a list of values for the number of attendees dropdown
        existing_data['number_of_attendees_values'].extend(
            [x for x in range(1, existing_data['max_attendees'] + 1)])

        # Create a form instance with the existing data
        form = BookingItemForm(
            max_attendees=item['experience'].max_attendees,
            initial=existing_data
        )

        # Append to forms
        forms.append({'experience': item['experience'], 'form': form})

    context = {
        'basket_items': forms,
        'total': basket_context['total'],
        'experience_count': basket_context['experience_count'],
        'discount': basket_context['discount'],
        'discount_delta': basket_context['discount_delta'],
        'discount_delivery_threshold': (
            basket_context['discount_delivery_threshold']),
        'grand_total': basket_context['grand_total'],
        'number_of_attendees_values': (
            existing_data['number_of_attendees_values']),
        'submitted_number_of_attendees': (
            existing_data.get('number_of_attendees', 0)),
    }

    template = 'basket/basket.html'

    return render(request, template, context)


# Assistance from CI - Boutique Ado walkthrough
def add_to_basket(request, item_id):
    """
    A view to add the number of attendees selected for
    an experience id to the basket
    """
    # Assistance from CI Tutor with addressing some issues with form validation
    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form = BookingItemForm(request.POST)

        if form.is_valid():
            # Proceed with adding products if form is valid
            number_of_attendees = form.cleaned_data['number_of_attendees']
            booking_time_slot = form.cleaned_data['booking_time_slot']

            # Check if the experience already exists in the basket
            if item_id in basket:
                messages.error(request, 'This experience already \
                    exists in your basket. If you wish to update it, please \
                        go to the basket to do so.')
                return redirect(redirect_url)
            else:
                # Add the experience to the basket
                basket[item_id] = {
                    'number_of_attendees': number_of_attendees,
                    'booking_date':  request.POST.get('booking_date'),
                    'max_attendees': request.POST.get('max_attendees'),
                    'booking_time_slot': booking_time_slot
                }

                request.session['basket'] = basket
                messages.success(request, 'Experience successfully added to \
                    your basket')

            return redirect(redirect_url)
        else:
            messages.error(request, 'Invalid form submission. Please check \
                your inputs')

            return redirect(redirect_url)


# Assistance from CI - Boutique Ado walkthrough
def adjust_basket(request, item_id):
    """
    A view to adjust the number of attendees, time slot or date in the
    line items of the basket
    """
    if request.method == 'POST':
        form = BookingItemForm(request.POST)

        if form.is_valid():
            # Proceed with adding products if form is valid
            number_of_attendees = form.cleaned_data['number_of_attendees']
            booking_time_slot = form.cleaned_data['booking_time_slot']
            booking_date = request.POST.get('booking_date', '')

            basket_item = request.session['basket'].get(item_id, {})
            basket_item['number_of_attendees'] = number_of_attendees
            basket_item['booking_time_slot'] = booking_time_slot
            basket_item['booking_date'] = booking_date

            request.session['basket'][item_id] = basket_item
            request.session.modified = True

            messages.success(request, 'Basket updated succesfully.')
        else:
            messages.error(request, 'Invalid form submission. Please \
                check your inputs.')
    else:
        messages.error(request, 'Invalid request method for adjusting basket')

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    A view to remove an item from the basket
    """
    try:
        if request.method == 'POST':
            basket = request.session.get('basket', {})
            print(f"Basket: {basket}")

            if item_id in basket:
                basket.pop(item_id)
                messages.success(request, 'Experience successfully removed \
                    from basket')
            else:
                messages.error(request, 'Whiskey Experience does not exist in \
                    basket')

            request.session['basket'] = basket
            return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
