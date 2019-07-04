from django import forms

from .models import Encabezado, Detalle


class BuscarCampoForm(forms.Form):
    texto = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Codigo de venta'}), required=False)

class EncabezadoForm(forms.ModelForm):
    class Meta:
        model = Encabezado
        fields = ('nombre_cliente',)

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = '__all__'