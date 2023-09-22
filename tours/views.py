# Assistance from CI - Boutique Ado walkthrough
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tours
from django.http import Http404


# Assistance from CI - Boutique Ado walkthrough
def all_tours(request):
    """
    A view to render all the tour experiences the company has to offer
    including search queries
    """
    tours = Tours.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('tours'))

            queries = Q(tour_name__icontains=query) | Q(
                    tour_description__icontains=query) | Q(
                        county__icontains=query) | Q(
                            post_code__icontains=query) | Q(
                            country__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'search_term': query
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
