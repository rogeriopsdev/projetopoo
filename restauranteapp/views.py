from django.shortcuts import render,redirect,get_object_or_404
from restauranteapp.forms import MesaForms
from .models import Mesa


# Create your views here.
def home(request):
    return render(request,'restaurante/home.html')


def index(request):
    mesas = Mesa.objects.all()
    return render(request, 'restaurante/index.html',{'mesas':mesas})

def salvar_mesa(request):
    form =MesaForms(request.POST)
    if request.method == "POST":
        form = MesaForms(request.POST, request.FILES)
        form.save()
        form=MesaForms()
    return render(request, 'restaurante/salvarmesa.html', {'form':form})


def editar_mesa(request,id):
    mesa =get_object_or_404(Mesa,pk=id)
    form =MesaForms(instance=mesa)
    if request.method == "POST":
        form = MesaForms(request.POST, request.FILES,instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesas')
        else:
            return render(request,'restaurante/editar_mesa.html',{'form':form,'mesa':mesa})
    else:
        return render(request, 'restaurante/editar_mesa.html', {'form': form, 'mesa': mesa})





def mesas(request):
    mesas = Mesa.objects.all()
    return render(request,"restaurante/mostrar_mesa.html",{'mesas':mesas})


def deletar(request,id):
    mesa = get_object_or_404(Mesa, pk=id)
    if request.method=="POST":
        mesa.delete()
        return redirect('mesas')
    return render(request,'restaurante/deletar.html',{'mesa':mesa} )

