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
    A view to add the quantity of an experience id to the basket
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
