from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.

def all_chai(request):
    chais = ChaiVarity.objects.all() # taking all the models of ChaiVarity in a single variable for use. This will return an Array of models 
    return render(request, 'chai/all_chai.html', {'chais':chais}) # This carly braces sends values in the frontend in form of dictionary