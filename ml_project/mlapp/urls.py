# mlapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Homepage'),
    path('homepage/',views.homepage,name='home'),
    path('models/',views.models,name='home'),
    path('contact/',views.contact,name='home'),
]
