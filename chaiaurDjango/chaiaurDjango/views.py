from django.http import HttpResponse
 
def home(request):
    return HttpResponse("Hello, world. You are at chai aur Django Home page")

def about(request):
    return HttpResponse("Hello, world. You are at chai aur Django About page")

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Django Contact page")