from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointmenthomepage, name='appointmenthomepage'),
    path('Aboutpage/', views.Aboutpage, name='Aboutpage'),
    path('Contactpage/', views.contactpage, name='Contactpage'),
    path('bookingpage/', views.bookingpage, name='bookingpage'),
]