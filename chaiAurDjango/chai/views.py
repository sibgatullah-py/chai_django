from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ChaiVaraity


def allChai(request):
    chais = ChaiVaraity.objects.all() # This will querry over chai models in database and give us an array of objects 
    return render(request, 'chai/allChai.html', {'chais': chais}) # also passing the models
                                            # name^ of data #^ filling variable
def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVaraity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})


# View Interacts with Models

# The view decides what data is needed.

# It communicates with the model layer (ORM).

# Models define your database schema (tables, fields, relationships).

# Django’s ORM (Object Relational Mapper) converts Python objects <-> database rows.