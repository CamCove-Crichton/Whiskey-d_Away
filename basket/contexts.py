# Assistance from CI - Boutique Ado walkthrough
from decimal import Decimal
from django.conf import settings


def basket_contents(request):
    """
    A function to return a dictionary of basket items
    """
    basket_items = []
    total = 0
    experience_count = 0

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
