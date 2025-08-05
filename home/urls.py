from django.contrib import admin
from django.urls import path
from home import views

# here the dispatching of urls is done
urlpatterns = [
    path("", views.index, name ='home'),
    path("home/", views.home, name='home'),
    path("about/", views.about, name ='about'),
    path("services/", views.services, name='services'),
    path("contacts/", views.contacts, name='contacts')
]