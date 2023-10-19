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
            messages.success(request, 'Profile successfully updated!')
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your mobile number and date of \
                birth are correct. Users/Applicants must be 18 or over')

    # Populate with users profile information
    form = UserProfileForm(instance=profile)

    # Get the users bookings
    bookings = profile.bookings.all()

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'bookings': bookings,
    }

    return render(request, template, context)
