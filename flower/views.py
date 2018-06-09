from django.shortcuts import render
from .models import Flower
# Create your views here.

def dashboard(request):
    return render(request, 'flower/dashboard.html', {
        'flowers': Flower.objects.all()
    } )
