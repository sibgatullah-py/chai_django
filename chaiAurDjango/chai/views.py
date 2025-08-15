from django.shortcuts import render

def allChai(request):
    return render(request, 'chai/allChai.html')