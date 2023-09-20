from django.shortcuts import render
from .models import Tours


# Assistance from CI - Boutique Ado walkthrough
def all_tours(request):
    """
    A view to render all the tour experiences the company has to offer
    including search queries
    """
    tours = Tours.objects.all()

    context = {
        'tours': tours
    }

    template = 'tours/tours.html'

    return render(request, template, context)
