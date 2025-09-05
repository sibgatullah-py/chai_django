
from django.urls import path
from .import views

urlpatterns = [
   path('',views.allChai,name='allChai'),
   path('<int:chai_id>/', views.chai_details, name='chai_details'),
   
]
