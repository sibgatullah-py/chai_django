from django.shortcuts import render, get_object_or_404
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm

# Create your views here.

def all_chai(request):
    chais = ChaiVarity.objects.all() # taking all the models of ChaiVarity in a single variable for use. This will return an Array of models 
    return render(request, 'chai/all_chai.html', {'chais':chais}) # This carly braces sends values in the frontend in form of dictionary

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)# This will take the object if not then this will show 404
    return render(request, 'chai/chai_details.html', {'chai':chai})# sending the data of the chai as objects in the html file 

def chai_stores_view(request):
    stores = None
    # Case1:- Submiting form
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)# This request.POST passing all the data travling in this post method in the form variable
        if form.is_valid():
            chai_variety =  form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else: form = ChaiVarityForm() # This is just a GET method form usually shown when the page is first loaded. 
    
    # Case2:- Rendering form 
    return render(request,'chai/chai_stores.html', {'stores':stores, 'form':form})