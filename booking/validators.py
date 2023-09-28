# Assistance from ChatGPT
from django.core.exceptions import ValidationError


def validate_number_of_attendees(value):
    """
    A function to raise a validation error if the value of the number of
    attendees is not from 1 to 8
    """
    if not 1 <= value <= 8:
        raise ValidationError('Number of attendees cannot be less than 1 or \
            more than 2, 4, 6 or 8 depending on the selected experience')
