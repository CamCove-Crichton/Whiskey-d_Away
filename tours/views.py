# Assistance from CI - Boutique Ado walkthrough
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Tours, Category
from booking.forms import BookingItemForm
from django.http import Http404


# Assistance from CI - Boutique Ado walkthrough
def all_tours(request):
    """
    A view to render all the tour experiences the company has to offer
    including category, sort and search queries
    """
    tours = Tours.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower('tour_name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tours = tours.filter(tour_category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'tours': tours,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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

    # Assistance from ChatGPT
    # Pass max_attendees to the booking form
    booking_form = BookingItemForm(max_attendees=tour.max_attendees)

    context = {
        'tour': tour,
        'booking_form': booking_form,
    }

    template = 'tours/tour_detail.html'

    return render(request, template, context)
