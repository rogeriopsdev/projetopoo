from django.shortcuts import render
from restauranteapp.forms import MesaForms


# Create your views here.
def index(request):
    form=MesaForms()
    return render(request, 'restaurante/index.html',{'form':form})

def salvar_mesa(request):
    form =MesaForms(request.POST)
    if request.method == "POST":
        form = MesaForms(request.POST, request.FILES)
        form.save()
        form=MesaForms()
    return render(request, 'restaurante/salvarmesa.html', {'form':form})

