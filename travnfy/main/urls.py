from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create_account/', views.create_account, name='create_account'),
    path('book_flights/', views.book_flights, name='book_flights'),
    path('book_cabs/', views.book_cabs, name='book_cabs'),
    path('book_trains/', views.book_trains, name='book_trains'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]
