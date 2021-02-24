from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(max_length=140, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
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
    