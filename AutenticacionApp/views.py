from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from  .forms import UsuarioForm,LoginForm

def Acceder(request):
    form =LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request,F"Bienvenido {nombre_usuario}")
                return render(request,"TesisApp/Inicio.html",{"message":nombre_usuario})
            else:
                messages.error(request,F"Datos incorrectos")                              
        else:
            messages.error(request,F"Los datos son incorrectos")
    return render(request,"TesisApp/Login.html",{"form":form})

def Registro(request):
    # Creamos el formulario de autenticación vacío
    form = UsuarioForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UsuarioForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    # Si llegamos al final renderizamos el formulario
    return render(request, "TesisApp/registro.html", {'form': form})  



     
def Inicio(request):
    return render(request,"TesisApp/Inicio.html")

def Logout(request):
    logout(request)
    messages.success(request,F"La sesion se ha cerrado")
    return redirect('Login')

def Login(request):
    return render(request,"TesisApp/Login.html")

def ConficUsu(request):
    return render(request,"TesisApp/config_usu.html")