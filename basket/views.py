from django.shortcuts import render, redirect


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

    number_of_attendees = int(request.POST.get('number_of_attendees'))
    booking_date = request.POST.get('booking_date')
    booking_time_slot = request.POST.get('booking_time_slot')
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if (isinstance(basket.get(item_id), dict) and
            'items_by_date_and_time' in basket[item_id]):
        if booking_date in basket[item_id]['items_by_date_and_time']:
            # The tour for the same day exists in the basket
            if (booking_time_slot in basket[item_id]
                    ['items_by_date_and_time'][booking_date]):
                # The tour for the same date and time slot already in basket
                (basket[item_id]['items_by_date_and_time']
                    [booking_date][booking_time_slot]) += number_of_attendees
            else:
                # Tour with same date exists but with differnt time slot
                (basket[item_id]['items_by_date_and_time']
                    [booking_date][booking_time_slot]) = number_of_attendees
        else:
            # The tour for a different date needs to be added
            basket[item_id]['items_by_date_and_time'][booking_date] = {
                booking_time_slot: number_of_attendees
            }
    else:
        # Tour is not in the basket so add it with specified date and time
        basket[item_id] = {
            'items_by_date_and_time': {
                booking_date: {
                    booking_time_slot: number_of_attendees
                }
            }
        }

    request.session['basket'] = basket
    return redirect(redirect_url)
