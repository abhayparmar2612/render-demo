from django.shortcuts import render
from django.http import JsonResponse
import joblib
import numpy as np
import pickle
from sklearn.metrics import r2_score

# Load the trained model
with open('../mdl.pkl','rb') as file:
    model = pickle.load(file)


with open('../second1.pkl','rb') as file1:
    nodel = pickle.load(file1)




    

    
# mlapp/views.py
def Index(request):
    return render(request,'index.html')


def Homepage(request):
    if request.method == 'POST':
        experience=request.POST.get('experience')
        experience = float(experience)

        
        
        

       

        pred = model.predict(np.array([[experience]]))
        pred=int(pred)
        

        return render(request,'home.html',{'pred':pred})

        
        

    else:
        return render(request,'home.html')


def Models(request):
    return render(request,'models.html')

def Contact(request):
    return render(request,'contact.html')


def success(request):
    return render(request,'success.html')


def second(request):

    if request.method == "POST":
        

        temperature = float(request.POST.get('temperature'))  # Convert to float

            # Ensure the temperature is valid
        predi = nodel.predict(np.array([[temperature]]))  
        
        return render(request, 'second.html', {'predi': predi})


    else:

        return render(request,'second.html')