# Assistance from ChatGPT
from django.db import models
from .utils import generate_unique_booking_number
from tours.models import Tours
from .validators import validate_number_of_attendees
from django.conf import settings


class Booking(models.Model):
    """
    A model to catpute all the bookings made by users
    """
    booking_number = models.CharField(
        max_length=10, unique=True, editable=False)
    date_of_booking = models.DateField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.booking_number

    def save(self, *args, **kwargs):
        """
        A method to overide the save method and assign the unique booking
        number to the booking number field in the model from the imported
        function for generating booking numbers
        """
        if not self.booking_number:
            self.booking_number = generate_unique_booking_number()
        super().save(*args, **kwargs)


class BookingItem(models.Model):
    """
    A model to capture line items of individual experiences for each booking
    """
    tour = models.ForeignKey(
        Tours, on_delete=models.SET_NULL,
        null=True, related_name='booking_items')
    number_of_attendees = models.IntegerField(
        validators=[validate_number_of_attendees], default=1)
    booking_date = models.DateField()
    booking_time_slot = models.CharField(
        max_length=11, choices=settings.TIME_SLOT_CHOICES)

    def __str__(self):
        return str(self.booking_date)
