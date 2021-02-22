from django.forms import ModelForm
from .models import Usuario
from django import forms

CHOICES= (
('1','Admin'),
('2','Usuario')
)

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['Usuario', 'Nombre','Apellido','Email','Contraseña','ReContraseña','Rol']
    Usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Contraseña = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ReContraseña = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Rol=forms.CharField(widget=forms.Select(attrs={'class': 'form-control'},choices=CHOICES))
 