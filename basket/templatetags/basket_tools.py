# Assistance from CI - Boutique Ado walkthrough
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, number_of_attendees):
    """
    A function to calculate the line item total
    """
    return price * number_of_attendees
