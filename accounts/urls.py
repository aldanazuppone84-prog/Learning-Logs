""" define URL mode for app acount"""
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # include the url for authentication
    path('', include('django.contrib.auth.urls')),
    # register
    path('register/', views.register, name='register'),
]