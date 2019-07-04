from django.db import models
from django.utils import timezone
from django.contrib import admin
from inventario.models import Producto

class Encabezado(models.Model):
    no_venta = models.AutoField(primary_key=True, unique=True)
    nombre_cliente = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.no_venta)

class Detalle(models.Model):
    encabezado_venta = models.ForeignKey(Encabezado, null=False, blank=False, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.PROTECT)
    cantidad = models.IntegerField(blank=False, null=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0.0)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0.0)
    observaciones = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.producto