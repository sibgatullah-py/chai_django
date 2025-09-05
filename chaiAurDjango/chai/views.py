from django.shortcuts import render
from .models import ChaiVaraity

def allChai(request):
    chais = ChaiVaraity.objects.all() # This will querry over chai models in database and give us the models 
    return render(request, 'chai/allChai.html', {'chais': chais}) # also passing the models