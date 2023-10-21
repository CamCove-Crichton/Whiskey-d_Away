# Assistance from CI - Boutique Ado Walkthrough
from django.urls import path
from . import views

# Assistance from CI - Boutique Ado Walkthrough
urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('tour_detail/<int:id>/', views.tour_detail, name='tour_detail'),
    path('add/', views.add_tour, name='add_tour'),
    path('edit/<int:tour_id>/', views.edit_tour, name='edit_tour'),
    path('delete/<int:tour_id>/', views.delete_tour, name='delete_tour'),
]
