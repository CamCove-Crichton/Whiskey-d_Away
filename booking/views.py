# Assistance from CI - Boutique Ado walkthrough
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import BookingForm


def booking(request):
    """
    A view to allow the user to create a booking
    """
    # Get the session basket
    basket = request.session.get('basket', {})

    # If not items are present, return error and return to tours
    if not basket:
        messages.error(request, 'No Experiences are currently \
                       in your basket')
        return redirect(reverse('tours'))
    
    # Create an empty booking form
    booking_form = BookingForm()

    # Assign a template
    template = 'booking/booking.html/'

    # Assign the context
    context = {
        'booking_form': booking_form,
        'stripe_public_key': 'pk_test_51NfFqdFriqsRUzVpVnU6nJjvMtcbGKZdEegmo6cvEgai1mzBWplAIk0kx9xCYVBW9n46Abvkp2HQYsPJlTQXlkAg00tqRXVShF',
    }

    # Return the rendered view
    return render(request, template, context)