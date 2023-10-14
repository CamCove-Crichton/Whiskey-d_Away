# Assistance from ChatGPT
from django.db import models
from django.db.models import Sum

from .utils import generate_unique_booking_number
from tours.models import Tours
from .validators import validate_number_of_attendees
from django.conf import settings

# A few fields assisted by CI - Boutique Ado walkthrough
class Booking(models.Model):
    """
    A model to catpute all the bookings made by users
    """
    booking_number = models.CharField(
        max_length=10, unique=True, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    mobile_number = models.CharField(max_length=20, null=False, blank=False)
    date_of_booking = models.DateTimeField(auto_now_add=True)
    discount_amount = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    booking_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    # Assistance from CI - Boutique Ado walkthrough
    def update_total(self):
        """
        Update the grand total each time a line item is added to the order
        accounting for the discount
        """
        self.booking_total = (self.lineitems.aggregate(Sum(
            'lineitem_total'))['lineitem_total__sum'] or 0)

        # Determine discount amount
        if self.booking_total > settings.DISCOUNT_SPEND_THRESHOLD:
            self.discount_amount = self.booking_total * settings.STANDARD_DISCOUNT_PERCENTAGE / 100
        else:
            self.discount_amount = 0

        # Calculate grand_total
        self.grand_total = self.booking_total - self.discount_amount
        self.save()

    # Assistance from ChatGPT
    def save(self, *args, **kwargs):
        """
        A method to overide the save method and assign the unique booking
        number to the booking number field in the model from the imported
        function for generating booking numbers
        """
        if not self.booking_number:
            self.booking_number = generate_unique_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number


# Assistance with adding the lineitem_total field from CI
# The Boutique Ado walkthrough
class BookingItem(models.Model):
    """
    A model to capture line items of individual experiences for each booking
    """
    tour = models.ForeignKey(
        Tours, on_delete=models.SET_NULL,
        null=True, related_name='booking_items')
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE,
        null=False, related_name='lineitems')
    number_of_attendees = models.IntegerField(
        validators=[validate_number_of_attendees], default=1)
    booking_date = models.DateField()
    booking_time_slot = models.CharField(
        max_length=11, choices=settings.TIME_SLOT_CHOICES)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    # Assistance from CI - Boutique Ado walkthrough
    def save(self, *args, **kwargs):
        """
        Overide the original save method to set the lineitem
        total and set the booking total
        """
        self.lineitem_total = self.tour.tour_price * self.number_of_attendees
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Experience: {self.tour.tour_name} in Booking No: {self.booking.booking_number}'
