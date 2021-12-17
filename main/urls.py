from django.urls import path
from main import views



urlpatterns = [
    path('',views.home, name="home"),
    path('about',views.about, name="about"),
    path('pricing',views.pricing, name="pricing"),
    path('contact',views.contact, name="contact"),
    path('services',views.services, name="services"),

     
]