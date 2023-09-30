from django.shortcuts import render, redirect


# Assistance from CI - Boutique Ado walkthrough
def view_basket(request):
    """
    A view to render the contents of the basket
    """
    return render(request, 'basket/basket.html')


# Assistance from CI - Boutique Ado walkthrough
def add_to_basket(request, item_id):
    """
    A view to add the number of attendees selected for
    an experience id to the basket
    """

    number_of_attendees = int(request.POST.get('number_of_attendees'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += number_of_attendees
    else:
        basket[item_id] = number_of_attendees

    request.session['basket'] = basket
    return redirect(redirect_url)
