from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from booking.forms import BookingItemForm
from tours.models import Tours


# Assistance from CI - Boutique Ado walkthrough
def view_basket(request):
    """
    A view to render the contents of the basket
    """
    return render(request, 'basket/basket.html')


# Assistance from CI - Boutique Ado walkthrough
def add_to_basket(request, item_id):
    """
    A view to add the number of attendees selected for
    an experience id to the basket
    """
    if request.method == 'POST':
        tour = get_object_or_404(Tours, id=item_id)
        booking_form = BookingItemForm(request.POST)
        redirect_url = request.POST.get('redirect_url')
        print(request.POST)
        print(booking_form.errors)
        print(booking_form)

        if booking_form.is_valid():
            number_of_attendees = (booking_form.cleaned_data
                                   ['number_of_attendees'])
            booking_date = booking_form.cleaned_data['booking_date']
            booking_time_slot = booking_form.cleaned_data['booking_time_slot']

            basket = request.session.get('basket', {})

            if (isinstance(basket.get(item_id), dict) and
                    'items_by_date_and_time' in basket[item_id]):
                if booking_date in basket[item_id]['items_by_date_and_time']:
                    # The tour for the same day exists in the basket
                    if (booking_time_slot in basket[item_id]
                            ['items_by_date_and_time'][booking_date]):
                        # Tour for same date and time slot already in basket
                        (basket[item_id]['items_by_date_and_time']
                            [booking_date]
                            [booking_time_slot]) += number_of_attendees
                    else:
                        # Tour with same date exists with different time slot
                        (basket[item_id]['items_by_date_and_time']
                            [booking_date]
                            [booking_time_slot]) = number_of_attendees
                else:
                    # The tour for a different date needs to be added
                    basket[item_id]['items_by_date_and_time'][booking_date] = {
                        booking_time_slot: number_of_attendees
                    }
            else:
                # Tour not in the basket so add it with specified date and time
                basket[item_id] = {
                    'items_by_date_and_time': {
                        booking_date: {
                            booking_time_slot: number_of_attendees
                        }
                    }
                }

            request.session['basket'] = basket
            return redirect(redirect_url)
        else:
            context = {
                'booking_form': booking_form,
                'tour': tour,
            }

            template = 'tours/tour_detail.html'

            return render(request, template, context)
