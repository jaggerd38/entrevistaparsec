from django.urls import path
from .views import *

from . import views


from django.urls import path, include


app_name = 'compras'

urlpatterns = [
    ##path('lista/', views.lista_productos, name="lista-productos"),
    ##path('nuevo/', views.agregar_producto, name='nuevo-producto'),
    ##path('<int:pk>/editar/', views.editar_producto, name='editar-producto'),
]