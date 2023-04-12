from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import InsumosForm, CocinaForm, BlancosForm
from .models import Insumos, Cocina, Blancos
# Create your views here.

def index(request):
    return render(request, 'main.html')

def inventario(request):
    return render(request, 'inventarios.html')
    
def inventario_insumos(request):
    return render(request, 'inventario-insumos.html')

def inventario_blancos(request):
    return render(request, 'inventario-blancos.html')

def inventario_cocina(request):
    return render(request, 'inventario-cocina.html')
    
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
def Cocina_view(request):
    
    form = CocinaForm()
    
    if request.method == 'POST':
        form = CocinaForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render( request,'registrar-entradac.html',context)


def listar_cocina(request):
    cocina = Cocina.objects.all().order_by('id')

    data = {
        'cocina':cocina
    }
    return render(request, 'inventario-cocina.html', data)


def editar_cocina(request,id):
    cocina = Cocina.objects.get(id=id)
    if request.method == 'GET':
        form = CocinaForm(instance=cocina)
    else:
        form = CocinaForm(request.POST, instance=cocina)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("listar_cocina"))
    return render(request, 'registrar-entradac.html', {'form':form})

def eliminar_cocina(request,id):
    cocina = Cocina.objects.get(id=id)
    if request.method == 'POST':
        cocina.delete()
        return HttpResponseRedirect(reverse("listar_cocina"))
    return render(request,'eliminar-cocina.html', {'cocina':cocina})

#------------------------------------------BLANCOS------------------------------------------
def Blancos_view(request):
    
    form = BlancosForm()
    
    if request.method == 'POST':
        form = BlancosForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render( request,'registrar-entradab.html',context)


def listar_blancos(request):
    blancos = Blancos.objects.all().order_by('id')

    data = {
        'blancos':blancos
    }
    return render(request, 'inventario-blancos.html', data)

def editar_blancos(request,id):
    blancos = Blancos.objects.get(id=id)
    if request.method == 'GET':
        form = BlancosForm(instance=blancos)
    else:
        form = BlancosForm(request.POST, instance=blancos)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("listar_blancos"))
    return render(request, 'registrar-entradab.html', {'form':form})

def eliminar_blancos(request,id):
    blancos = Blancos.objects.get(id=id)
    if request.method == 'POST':
        blancos.delete()
        return HttpResponseRedirect(reverse("listar_blancos"))
    return render(request,'eliminar-blancos.html', {'blancos':blancos})
