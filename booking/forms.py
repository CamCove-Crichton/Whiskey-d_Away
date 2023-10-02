# Assistance from ChatGPT
from django import forms
from django.core.exceptions import ValidationError
from .models import BookingItem
from django.utils import timezone
from django.conf import settings


class BookingItemForm(forms.ModelForm):
    """
    A form for to capture the user input for the selected whiskey experience
    """
    class Meta:
        model = BookingItem
        fields = ['number_of_attendees', 'booking_date', 'booking_time_slot']

    def clean_booking_date(self):
        """
        A validation to check the booking date selected is not in the past
        """
        booking_date = self.cleaned_data['booking_date']
        if booking_date < timezone.now().date():
            raise ValidationError('Booking date cannot be in the past.')
        return booking_date

    def clean_booking_time_slot(self):
        """
        A validtion to check the time slot selected is in the future, and if
        not then will raise a validation error
        """
        booking_time_slot = self.cleaned_data['booking_time_slot']
        booking_date = self.cleaned_data['booking_date']
        current_datetime = timezone.now()

        # Check if selected time slot is in TIME_SLOT_CHOICES
        if booking_time_slot not in [
            choice[0] for choice in settings.TIME_SLOT_CHOICES
        ]:
            raise ValidationError('Invalid time slot')

        # Loop through TIME_SLOT_CHOICES to find start time for selected slot
        start_time = None
        for choice in settings.TIME_SLOT_CHOICES:
            if choice[0] == booking_time_slot:
                start_time = timezone.datetime.strptime(
                    choice[1].split('-')[0].strip(), '%I:%M %p').time()
                break

        if not start_time:
            raise ValidationError('Start time not found for the selected \
                time slot')

        # Combine selected date and start time to create a datetime object
        slot_datetime = timezone.datetime.combine(booking_date, start_time)

        # Check if the booking slots datetime is not in the past
        if current_datetime > slot_datetime:
            raise ValidationError('This time slot is no longer available')

        return booking_time_slot
