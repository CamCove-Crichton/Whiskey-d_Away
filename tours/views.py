from django.shortcuts import render, get_object_or_404
from .models import Tours
from django.http import Http404


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


def tour_detail(request, id):
    """
    A view to display the full details of an individual tour experience
    """
    try:
        tour = get_object_or_404(Tours, id=id)
    except Tours.DoesNotExist:
        raise Http404("Tour does not exist")

    context = {
        'tour': tour
    }

    template = 'tours/tour_detail.html'

    return render(request, template, context)
