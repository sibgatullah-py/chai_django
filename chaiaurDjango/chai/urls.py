
from django.urls import path
from . import views

urlpatterns = [
   # path('order/', views.order, name='order'),
   path('',views.all_chai, name='all_chai'),
   path('<int:chai_id>/',views.chai_details, name='chai_details')
]