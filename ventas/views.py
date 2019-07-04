from django.shortcuts import render


from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from .models import Encabezado, Detalle
from django.http import HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.urls import reverse
from urllib.parse import urlencode
from .forms import EncabezadoForm, BuscarCampoForm


#@login_required()
def lista_ventas(request):
    template = 'orden_compra/lista_orden_compra.html'
    encabezado_lista = Encabezado.objects.all().order_by('-id')
    paginator = Paginator(encabezado_lista, settings.REGISTROS_PAGINA)

    form = BuscarCampoForm()
    if request.method == 'GET':
        form = BuscarCampoForm(request.GET)
        if form.is_valid():
            codigo = form.cleaned_data['texto']
    if codigo:
        ordenescompra = Encabezado.objects.filter(no_venta=codigo).order_by('-id')
    else:
        page = request.GET.get('page')
        try:
            ordenescompra = paginator.get_page(page)
        except PageNotAnInteger:
            ordenescompra = paginator.get_page(1)
        except EmptyPage:
            ordenescompra = paginator.get_page(paginator.get_num_pages)

    return render(request, template, locals())

#@login_required()
def nueva_venta(request):
    template = 'orden_compra/editar_orden_compra.html'
    if request.method == "POST":
        form = EncabezadoForm(request.POST)
        if form.is_valid():
            #fecha_recibida = form.cleaned_data['fecha']

            detalle = form.save(commit=False)
            detalle.fecha = timezone.now()
            detalle.save()
            return redirect('ventas:detalle-venta', pk = detalle.no_venta)
    else:
        form = EncabezadoForm()
    context = {'form': form, 'asunto': 'Nueva'}
    return render(request, template, context)

#@login_required()
def detalle_venta(request, pk):
    template = 'orden_compra/detalle_orden_compra.html'
    venta = get_object_or_404(Encabezado, no_venta=pk)
    
    
    #detalles_lista = Detalle.objects.filter(producto=pk).order_by('-id')
    #paginator = Paginator(detalles_lista, settings.REGISTROS_PAGINA)
    detalles = Detalle.objects.filter(producto=pk).order_by('-id')

    

    context = {'orden': venta, 'detalles': detalles}
    return render(request, template, context)

#@login_required()
def nuevo_detalle_venta(request, pk):
   template = 'orden_compra/editar_detalle_orden.html'
   venta = get_object_or_404(Encabezado, no_venta=pk)
   if request.method == "POST":
       form = DetalleForm(request.POST)
       if form.is_valid():
           detalle = form.save(commit=False)
           detalle.encabezado_venta = get_object_or_404(Encabezado, no_venta=pk)
           detalle.save()
           return redirect('ventas:detalle-venta', pk = detalle.no_venta)
   else:
       form = DetalleForm()
   return render(request, template, {'form': form, 'asunto':'Nuevo','orden':venta})    