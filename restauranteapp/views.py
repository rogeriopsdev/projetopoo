from django.shortcuts import render
from restauranteapp.forms import MesaForms


# Create your views here.
def index(request):
    form=MesaForms()
    return render(request, 'restaurante/index.html',{'form':form})
