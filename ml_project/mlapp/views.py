from django.shortcuts import render
from django.http import JsonResponse
import pickle
import numpy as np

# Load the trained model
with open('../model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(request):
    # Example input data (replace with actual request data)
    input_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Sample input for Iris dataset

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Return the prediction as a JSON response
    return JsonResponse({'prediction': prediction.tolist()})

# Create your views here.
# mlapp/views.py

