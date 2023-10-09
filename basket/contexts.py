from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Tours
from booking.forms import BookingItemForm


def basket_contents(request):
    """
    A function to return a dictionary of basket items
    """
    # Initialise empty lists and variables to store basket information
    basket_items = []
    total = 0
    experience_count = 0
    discount = 0
    discount_delta = 0
    grand_total = 0

    # Get the basket from the session,
    # Default to empty dictionary if it is not present
    basket = request.session.get('basket', {})

    # Iterate through each item in the basket
    for item_id, item_data in basket.items():
        # Retrieve relevant info for the item from the session data
        number_of_attendees = item_data.get('number_of_attendees', 0)
        booking_time_slot = item_data.get('booking_time_slot', '')
        booking_date = item_data.get('booking_date', '')
        max_attendees = item_data.get('max_attendees', 0)

        # Retrieve corresponding experience object from the database
        experience = get_object_or_404(Tours, pk=item_id)

        # Calculate the total cost line item
        total += number_of_attendees * experience.tour_price

        # Update the count based on number of attendees in the basket
        experience_count += number_of_attendees

        # Append a dictionary representing the item to the basket_items list
        basket_items.append({
            'item_id': item_id,
            'number_of_attendees': number_of_attendees,
            'booking_time_slot': booking_time_slot,
            'booking_date': booking_date,
            'max_attendees': max_attendees,
            'experience': experience,
            'total': total,
        })

    # Check if the total exceeds the discount threshold
    if total >= settings.DISCOUNT_SPEND_THRESHOLD:
        # Calculate the discount amount
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE/100)

        # Calculate the remaining amount needed to qualify for the discount
        discount_delta = settings.DISCOUNT_SPEND_THRESHOLD - total

    # Calculate the grand total after applying the discount
    grand_total = total - discount

    # Create a dictionary containing all the values
    context = {
        'basket_items': basket_items,
        'total': total,
        'experience_count': experience_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_delivery_threshold': settings.DISCOUNT_SPEND_THRESHOLD,
        'grand_total': grand_total,
    }

    # return context
    return context
