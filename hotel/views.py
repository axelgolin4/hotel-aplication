from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import InsumosForm
from .models import Insumos
# Create your views here.

def index(request):
    return render(request, 'main.html')

def inventario(request):
    return render(request, 'inventarios.html')
    
def inventario_insumos(request):
    return render(request, 'inventario-insumos.html')

def registrar_entrada(request):
    return render(request, 'registrar-entrada.html')

def registrar_salida(request):
    return render(request, 'registrar-salida.html')


#------------------------------------------INGRESOS------------------------------------------

def Insumos_view(request):
    
    form = InsumosForm()
    
    if request.method == 'POST':
        form = InsumosForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render( request,'registrar-entrada.html',context)


def listar_insumos(request):
    insumos = Insumos.objects.all().order_by('id')

    data = {
        'insumos':insumos
    }
    return render(request, 'inventario-insumos.html', data)

def editar_insumos(request,id):
    insumos = Insumos.objects.get(id=id)
    if request.method == 'GET':
        form = InsumosForm(instance=insumos)
    else:
        form = InsumosForm(request.POST, instance=insumos)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("listar_insumos"))
    return render(request, 'registrar-entrada.html', {'form':form})

def eliminar_insumos(request,id):
    insumos = Insumos.objects.get(id=id)
    if request.method == 'POST':
        insumos.delete()
        return HttpResponseRedirect(reverse("listar_insumos"))
    return render(request,'eliminar-insumos.html', {'insumos':insumos})

#------------------------------------------COCINA------------------------------------------

