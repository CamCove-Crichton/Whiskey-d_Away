from django.shortcuts import render, redirect, get_object_or_404
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

    # Iterate through basket items
    for item in basket_items:
        # Get existing data for the current item
        existing_data = {
            'number_of_attendees': item['number_of_attendees'],
            'booking_date': item['booking_date'],
            'booking_time_slot': item['booking_time_slot'],
            'experience': item['experience'],
        }

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
    }

    template = 'basket/basket.html'

    return render(request, template, context)


# Assistance from CI - Boutique Ado walkthrough
def add_to_basket(request, item_id):
    """
    A view to add the number of attendees selected for
    an experience id to the basket
    """
    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form = BookingItemForm(request.POST)

        if form.is_valid():
            # Proceed with adding products if form is valid
            number_of_attendees = form.cleaned_data['number_of_attendees']
            # booking_date = form.cleaned_data['booking_date']
            booking_time_slot = form.cleaned_data['booking_time_slot']
            # max_attendees = form.cleaned_data.get('max_attendees')

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
            print(f"Form errors: {form.errors}")
            return redirect(redirect_url)


# Assistance from CI - Boutique Ado walkthrough
def adjust_basket(request, item_id):
    """
    A view to aadjust the number of attendees, time slot or date in the
    line items of the basket
    """
    try:
        number_of_attendees = int(request.POST.get('number_of_attendees'))
    except ValueError:
        messages.error(request, 'Invalid number of attendees. \
            Please enter a valid number.')
        return redirect(reverse('view_basket'))

    item_data = {}

    booking_date = request.POST.get('booking_date')
    booking_time_slot = request.POST.get('booking_time_slot')
    basket = request.session.get('basket', {})

    # Check if basket[item_id] is a dictionary
    if (isinstance(basket.get(item_id), dict) and
            'items_by_date_and_time' in basket[item_id]):
        # The item is already in the basket
        item_data = basket[item_id]

        # Assistance from tutor at CI
        item_data = {
            'items_by_date_and_time': {
                booking_date: {
                    booking_time_slot: number_of_attendees
                }
            }
        }

    # Update the session variable with the modified basket
    request.session['basket'][item_id] = item_data
    # Assistance from tutor at CI
    request.session.modified = True

    messages.success(request, 'Basket successfully updated')
    return redirect(reverse('view_basket'))
