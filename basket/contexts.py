# Assistance from CI - Boutique Ado walkthrough
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Tours
from booking.forms import BookingItemForm


def basket_contents(request):
    """
    A function to return a dictionary of basket items
    """
    basket_items = []
    total = 0
    experience_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, dict) and (isinstance(
                item_data.get('items_by_date_and_time'), dict)):
            if 'items_by_date_and_time' in item_data:
                for (date,
                        time_slots) in (item_data[
                            'items_by_date_and_time'].items()):
                    for time_slot, number_of_attendees in time_slots.items():
                        experience = get_object_or_404(Tours, pk=item_id)
                        total += number_of_attendees * experience.tour_price
                        experience_count += number_of_attendees
                        basket_items.append({
                            'item_id': item_id,
                            'number_of_attendees': number_of_attendees,
                            'booking_date': date,
                            'booking_time_slot': time_slot,
                            'experience': experience,
                            'total': total,
                        })

    if total >= settings.DISCOUNT_SPEND_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE/100)
        discount_delta = settings.DISCOUNT_SPEND_THRESHOLD - total
    else:
        discount = 0
        discount_delta = 0

    grand_total = total - discount

    context = {
        'basket_items': basket_items,
        'total': total,
        'experience_count': experience_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_delivery_threshold': settings.DISCOUNT_SPEND_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
