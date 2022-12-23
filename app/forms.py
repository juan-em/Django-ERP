from django import forms
from django.forms import ModelForm
from .models import *



class ProveedorBusqueda(ModelForm):
    class Meta:
        model = Persona
        # fields = '__all__'
        fields = ('id', 'dni', 'nombre', 'telefono', 'codprovincia', 'localidad')
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'codprovincia': forms.Select(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'})
        }

class ClienteBusqueda(ModelForm):
    class Meta:
        model = Persona
        # fields = '__all__'
        fields = ('id', 'dni', 'nombre', 'telefono', 'codprovincia', 'localidad')
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'codprovincia': forms.Select(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProveedorAgregar(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'dni':forms.TextInput(attrs={'class': 'form-control'}),
            'codprovincia':forms.Select(attrs={'class':'form-select form-select-sm'}),
            'localidad':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control'}),
            'codpostal':forms.TextInput(attrs={'class': 'form-control'}),
            'cuentabancaria':forms.TextInput(attrs={'class': 'form-control'}),
            'telefono':forms.TextInput(attrs={'class': 'form-control'}),
            'movil':forms.TextInput(attrs={'class': 'form-control'}),
            'web':forms.TextInput(attrs={'class': 'form-control'}),
        }
