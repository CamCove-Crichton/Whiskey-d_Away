# Assistance from ChatGPT
import uuid


# Assistance from ChatGPT
def generate_unique_booking_number():
    """
    A function to generate a unique booking number, and check if it exists
    in the database or not
    """
    # Import the Booking model in the function to prevent circular import
    from .models import Booking

    while True:
        booking_number = str(uuid.uuid4().hex)[:10]
        # We then check if the booking number exists in the Booking objects
        if not Booking.objects.filter(booking_number=booking_number).exists():
            return booking_number
