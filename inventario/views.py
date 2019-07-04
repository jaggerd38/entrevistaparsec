from django.shortcuts import render, render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ProductosForm
from .models import Producto
from django.contrib.auth.decorators import login_required



def lista_productos(request):
    template = 'producto/lista_productos.html'
    productos_lista = Producto.objects.all().order_by('-id')

    context = {'productos': productos_lista,}

    print(productos_lista)

    return render(request, template, context)

##@login_required()
def agregar_producto(request):
    template = 'producto/editar_producto.html'
    if request.method == "POST":
        form = ProductosForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario_creacion = request.user
            producto.usuario_modificacion = request.user
            producto.save()
            return render(request, template, {'form': form})
    else:
        form = ProductosForm()
    return render(request, template, {'form': form})

##@login_required()
def editar_producto(request, pk):
    template = 'producto/editar_producto.html'
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return render(request, template, {'form': form})
    else:
        form = ProductosForm(instance=producto)
    return render(request, template, {'form': form})