from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.index, name="Aboutus"),
    path("contact/", views.index, name="Contactus"),
    path("tracker/", views.index, name="TrackingStatus"),
    path("search/", views.index, name="Search"),
    path("productview/", views.index, name="ProductView"),
    path("checkout/", views.index, name="Checkout"), 
]