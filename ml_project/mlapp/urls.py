# mlapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('home/',views.Homepage,name='home'),
    path('models/',views.Models,name='models'),
    path('contact/',views.Contact,name='contact'),
    path('success/',views.success,name='success'),
    path('second/',views.second,name='second'),
]
