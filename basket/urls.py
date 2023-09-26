# Assistance from CI - Boutique Ado Walkthrough
from django.urls import path
from . import views

# Assistance from CI - Boutique Ado Walkthrough
urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
