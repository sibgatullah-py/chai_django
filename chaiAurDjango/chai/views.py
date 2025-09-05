from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ChaiVaraity


def allChai(request):
    chais = ChaiVaraity.objects.all() # This will querry over chai models in database and give us the models 
    return render(request, 'chai/allChai.html', {'chais': chais}) # also passing the models

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVaraity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})