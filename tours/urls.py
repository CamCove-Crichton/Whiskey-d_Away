# Assistance from CI - Boutique Ado Walkthrough
from django.urls import path
from . import views

# Assistance from CI - Boutique Ado Walkthrough
urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('tour_detail/<int:id>/', views.tour_detail, name='tour_detail'),
]
