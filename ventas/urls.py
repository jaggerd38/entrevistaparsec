from django.urls import path
from .views import *

from . import views


from django.urls import path, include


app_name = 'ventas'

urlpatterns = [
    path('lista/', views.lista_ventas, name="lista-ventas"),
    path('nueva/', views.nueva_venta, name='nueva-venta'),
    #path('<int:pk>/editar/', views.editar_orden_compra, name='editar-orden-compra'),
    path('<int:pk>/detalle/', views.detalle_venta, name='detalle-venta'),
    path('<int:pk>/nuevo-detalle/', views.nuevo_detalle_venta, name='nuevo-detalle-venta'),
    ##path('nuevo/', views.agregar_producto, name='nuevo-producto'),
    ##path('<int:pk>/editar/', views.editar_producto, name='editar-producto'),
]