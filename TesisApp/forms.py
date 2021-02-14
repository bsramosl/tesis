from django.forms import ModelForm
from .models import Usuario
from django import forms


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['Usuario', 'Nombre','Apellido','Email','Contraseña','ReContraseña']
    Usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Contraseña = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ReContraseña = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   