from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


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

            messages.success(request, 'Profile successfully updated!')
        else:
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

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'bookings': bookings,
    }

    return render(request, template, context)

def booking_history(request, booking_number):
    """
    A view to render the booking history details
    """

