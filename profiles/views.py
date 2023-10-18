from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    A view to render the users details
    """
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)

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
