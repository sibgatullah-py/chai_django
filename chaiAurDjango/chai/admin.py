# with admin.py we can attach any models and see in admin 
from django.contrib import admin
from .models import ChaiVaraity

# Register your models here.
admin.site.register(ChaiVaraity)
