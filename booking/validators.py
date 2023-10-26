# Assistance from ChatGPT
from django.core.exceptions import ValidationError
from django.db.models import Sum


def validate_number_of_attendees(value):
    """
    A function to raise a validation error if the value of the number of
    attendees is not from 1 to 8
    """
    if value < 1 or value > 8:
        raise ValidationError('Number of attendees cannot be less than 1 or \
            more than 2, 4, 6 or 8 depending on the selected experience')


# def is_time_slot_available(
#     booking_date,
#     booking_time_slot,
#     number_of_attendees,
#     tour_id
# ):
#     """
#     A function to check if the time slot selected is available
#     """
#     from .models import BookingItem
#     from tours.models import Tours
#     # Query the database for the total number of attendees for
#     # the specified time slot and date
#     total_attendees = BookingItem.objects.filter(
#         booking_date=booking_date,
#         booking_time_slot=booking_time_slot,
#         tour_id=tour_id,
#     ).aggregate(Sum('number_of_attendees'))['number_of_attendees__sum']

#     # If no bookings for that time slotand date or the total number
#     # of attendees plus the new attendees are less or equal to the
#     # max capacity then the time slot is available
#     tour = Tours.objects.get(pk=tour_id)
#     max_capacity = tour.max_capacity

#     return (
#         total_attendees is None or
#         (total_attendees + number_of_attendees) <= max_capacity
#     )
