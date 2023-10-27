# Assistance from CI - Boutique Ado Walkthrough
from django.urls import path
from . import views

# Assistance from CI - Boutique Ado Walkthrough
urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us'),
]
