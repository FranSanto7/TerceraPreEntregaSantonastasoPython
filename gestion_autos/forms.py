from django import forms
from .models import Marca, Modelo

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre', 'año', 'marca']