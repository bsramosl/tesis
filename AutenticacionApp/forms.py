from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class UsuarioForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre',max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(label='Apellido',max_length=140, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'controls','placeholder':'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'controls','placeholder':'Contraseña'}))
  
    class Meta:
        model = User
        fields = (
            'username',
            'password',  
        )

class ContraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UsuForm(ModelForm):
    first_name = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(max_length=140, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))   
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CheckboxInput()    

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_superuser'           
        )

