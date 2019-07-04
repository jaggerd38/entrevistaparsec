from django.db import models
from django.utils import timezone
from django.contrib import admin

class Producto(models.Model):
    codigo_de_barras = models.CharField(max_length=12, blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(default='', blank=True, null=True)
    precio_venta_uno = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0.0)
    precio_venta_dos = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0.0)
    precio_costo = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0.0)
    observaciones = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.nombre