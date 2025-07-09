from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def prog03(request):
    return render(request, 'prog03.html')

