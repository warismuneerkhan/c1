from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('icecream/',views.Icecream, name='icecream'),
    path('contact/',views.contact, name = 'contact')
    

]