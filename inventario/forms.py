from django import forms
from django.db.models import Q
from .models import Producto

class FiltrarMedidasForm(forms.Form):
    texto = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Medida'}), required=False)

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
                'codigo_de_barras',
                'nombre',
                'descripcion',
                'precio_venta_uno',
                'precio_venta_dos',
                'precio_costo',
                'observaciones',)