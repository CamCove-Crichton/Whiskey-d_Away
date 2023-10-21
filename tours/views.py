# Assistance from CI - Boutique Ado walkthrough
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Tours, Category
from .forms import ToursForm
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
    print('BASKET: ', request.session.get('basket'))
    # request.session['basket'] = {}
    try:
        tour = get_object_or_404(Tours, id=id)
    except Tours.DoesNotExist:
        raise Http404("Tour does not exist")

    # Assistance from ChatGPT
    # Pass max_attendees to the booking form
    booking_form = BookingItemForm(max_attendees=tour.max_attendees)

    # Assistance from CI Tutor with generating the number of attendees list
    context = {
        'tour': tour,
        'booking_form': booking_form,
        'number_of_attendees': [x for x in range(1, tour.max_attendees + 1)]
    }

    template = 'tours/tour_detail.html'

    return render(request, template, context)


def add_tour(request):
    """
    A view for the admin to add tour experiences
    """
    # Check if the request is POST
    if request.method == 'POST':

        # Assign the form with the post and files data
        form = ToursForm(request.POST, request.FILES)

        # Check if the form is valid
        if form.is_valid():
            # Save the form and return a success message
            tour = form.save()
            messages.success(request, 'Experience successfully \
                added to Tour offerings!')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            # Otherwise return an error message
            messages.error(request, 'Failed to add Experience. \
                Please check all form inputs are valid!')
    else:
        # If request is not POST, initiate an empty form
        form = ToursForm()

    # Assign the template
    template = 'tours/add_tour.html'

    # Assign the context
    context = {
        'form': form,
    }

    # Render the view
    return render(request, template, context)


def edit_tour(request, tour_id):
    """
    A view to allow admin users to edit the
    existing experiences in the database
    """
    # Assign the tour using get_object_or_404 with the id
    tour = get_object_or_404(Tours, pk=tour_id)

    # Check if the request is POST
    if request.method == 'POST':
        form = ToursForm(
            request.POST,
            request.FILES,
            instance=tour
        )

        if form.is_valid():
            form.save()
            messages.success(request, f'{tour.tour_name} \
                successfully updated!')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(request, f'Failed to update \
                {tour.tour_name}. Please check all your \
                form inputs are valid!')
    else:
        # Initiate the form with the instance of the tour
        form = ToursForm(instance=tour)

        # Inform the admin user they are editing a tour experience
        messages.info(request, f'You are editing {tour.tour_name}')

    # Assign the template
    template = 'tours/edit_tour.html'

    # Assign the context
    context = {
        'form': form,
        'tour': tour,
    }

    # Render the view
    return render(request, template, context)


def delete_tour(request, tour_id):
    """
    A view to allow admin users to remove
    tour experiences from the database
    """
    # Get the tour using get_object_or_404
    tour = get_object_or_404(Tours, pk=tour_id)
    
    # Delete the tour & return a success message
    tour.delete()
    messages.success(request, f'{tour.tour_name} \
        successfully deleted!')
    return redirect(reverse('tours'))
