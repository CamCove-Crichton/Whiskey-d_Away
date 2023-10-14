# Assistance from CI - Boutique Ado Walkthrough
from django.urls import path
from . import views
from .webhooks import webhook

# Assistance from CI - Boutique Ado Walkthrough
urlpatterns = [
    path('', views.booking, name='booking'),
    path('booking_success/<booking_number>/', views.booking_success, name='booking_success'),
    path('wh/', webhook, name='webhook'),
]
