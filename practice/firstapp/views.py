from django.shortcuts import render

# Create your views here.
def htmlHome(request):
    return render(request, 'firstapp/index.html')