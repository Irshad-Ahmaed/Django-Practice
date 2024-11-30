from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, chaiStore
from .forms import ChaiVarietyForm

# Create your views here.
def htmlHome(request):
    return render(request, 'firstapp/index.html')

def get_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'firstapp/chais.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'firstapp/chai_detail.html', {'chai': chai})

def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = chaiStore.objects.filter(chai_varieties = chai_variety)
    else:
        form = ChaiVarietyForm()

    return render(request, 'firstapp/chai_stores.html', {'stores': stores, 'form': form})