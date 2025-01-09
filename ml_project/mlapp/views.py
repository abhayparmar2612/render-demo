from django.shortcuts import render
from django.http import JsonResponse
import pickle
import numpy as np

# Load the trained model



# mlapp/views.py
def home(request):
    return render(request,'index.html')


def homepage(request):
    return render(request,'home.html')


def models(request):
    return render(request,'models.html')

def contact(request):
    return render(request,'contact.html')

