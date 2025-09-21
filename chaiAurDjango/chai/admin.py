# with admin.py we can attach any models and see in admin 
from django.contrib import admin
from .models import ChaiVaraity #importing the model (ChaiVarity) from models.py

# Register your models here.
admin.site.register(ChaiVaraity)
