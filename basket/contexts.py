# Assistance from CI - Boutique Ado walkthrough
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Tours


def basket_contents(request):
    """
    A function to return a dictionary of basket items
    """
    basket_items = []
    total = 0
    experience_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        experience = get_object_or_404(Tours, pk=item_id)
        total += quantity * experience.tour_price
        experience_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
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
