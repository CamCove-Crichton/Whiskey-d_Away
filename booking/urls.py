# Assistance from CI - Boutique Ado Walkthrough
from django.urls import path
from . import views

# Assistance from CI - Boutique Ado Walkthrough
urlpatterns = [
    path('', views.booking, name='booking'),
    path('booking_success/<booking_number>/', views.booking_success, name='booking_success'),
]
