from django.shortcuts import render, redirect
from .models import Marca, Modelo
from .forms import MarcaForm, ModeloForm

def index(request):
    modelos = Modelo.objects.all()
    return render(request, 'gestion_autos/index.html', {'modelos': modelos})

def agregar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MarcaForm()
    return render(request, 'gestion_autos/agregar_marca.html', {'form': form})

def agregar_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ModeloForm()
    return render(request, 'gestion_autos/agregar_modelo.html', {'form': form})

def buscar(request):
    query = request.GET.get('q')
    if query:
        resultados = Modelo.objects.filter(nombre__icontains=query) | Modelo.objects.filter(marca__nombre__icontains=query)
    else:
        resultados = None
    return render(request, 'gestion_autos/buscar.html', {'resultados': resultados})
