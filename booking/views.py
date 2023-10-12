# Assistance from CI - Boutique Ado walkthrough
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import BookingForm
from basket.contexts import basket_contents

import stripe


def booking(request):
    """
    A view to allow the user to create a booking
    """
    # Assistance from CI - Boutique Ado walkthrough
    # Assign stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
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
