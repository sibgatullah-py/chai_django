from django.contrib import admin
from django.urls import path, include
from .import views

from django.conf import settings # bringing settings file 
from django.conf.urls.static import static # for loading media root and media 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('chai/',include('chai.urls')),# expanding urls of chai app
    
    
    path("__reload__/", include("django_browser_reload.urls")),# for live browser refresh during development
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
