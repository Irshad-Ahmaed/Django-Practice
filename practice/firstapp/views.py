from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def htmlHome(request):
    return render(request, 'firstapp/index.html')

def get_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'firstapp/chais.html', {'chais': chais})