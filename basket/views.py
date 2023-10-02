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

        number_of_attendees = int(request.POST.get('number_of_attendees'))
        redirect_url = request.POST.get('redirect_url')
        basket = request.session.get('basket', {})

        if item_id in list(basket.keys()):
            basket[item_id] += number_of_attendees
        else:
            basket[item_id] = number_of_attendees

                request.session['basket'] = basket
                return redirect(redirect_url)
            else:
                context = {
                    'booking_form': booking_form,
                    'tour': tour,
                }

                template = 'tours/tour_detail.html'

                return render(request, template, context)
