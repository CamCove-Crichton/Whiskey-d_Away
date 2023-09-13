from django.shortcuts import render


# Assistance from CI - Boutique Ado walkthrough
def index(request):
    """
    A view to render the index template
    """
    return render(request, 'home/index.html')
