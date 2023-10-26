from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from booking.models import Booking


@login_required
def profile(request):
    """
    A view to render the users details
    """
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if the request method is POST
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        # Check if the form is valid
        if form.is_valid():
            form.save()

            # Save additional fields to the User model
            user = User.objects.get(pk=request.user.pk)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            # Return a success message to the user
            messages.success(request, 'Profile successfully updated!')
        else:
            # Return error message to the user
            messages.error(request, 'There was an error with your form. \
                Please double check your mobile number and date of \
                birth are correct. Users/Applicants must be 18 or over')
    else:
        # Assistance from ChatGPT
        # Populate with users profile information
        form = UserProfileForm(instance=profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })

    # Get the users bookings
    bookings = profile.bookings.all()

    # Assign the template
    template = 'profiles/profile.html'

    # Assign the context
    context = {
        'form': form,
        'bookings': bookings,
    }

    # Render the view
    return render(request, template, context)


def booking_history(request, booking_number):
    """
    A view to render the booking history details
    """
    # Get the booking object from the booking number
    booking = get_object_or_404(
                Booking, booking_number=booking_number)

    # Display a message to the user
    messages.info(request, (
        f'This is a previous booking confirmation \
        for booking number {booking_number}.'
        f'A confirmation email was sent to {booking.email} \
        on {booking.date_of_booking}.'
        ))

    # Assign the template
    template = 'booking/booking_success.html/'

    # Assign the context
    context = {
        'booking': booking,
        'from_profile': True,
    }

    # Render the view
    return render(request, template, context)
