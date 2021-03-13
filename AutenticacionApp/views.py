from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from  .forms import UsuarioForm, LoginForm ,ContraseñaForm,UsuForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
import numpy as np

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
                messages.error(request,form.errors)                              
        else:
            messages.error(request,form.errors)
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
            messages.success(request,'Usuario registrado')  
            return redirect('Login')
        else:
            messages.error(request, form.errors)
    # Si llegamos al final renderizamos el formulario
    return render(request, "TesisApp/registro.html", {'form': form})  

def cambiar_contraseña(request):
    if request.method == 'POST':
        form = ContraseñaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña ha sido cambiada.')
            return redirect('Inicio')
        else:
            messages.error(request,form.errors)
    else:
        form = ContraseñaForm(request.user)
    return render(request, "TesisApp/config_usu.html", {'form': form})

class Crud():

    def edit(request,id):
        # Recuperamos la instancia de la persona
        instancia = User.objects.get(id=id)
        # Creamos el formulario con los datos de la instancia
        form = UsuForm(instance=instancia)
        # Comprobamos si se ha enviado el formulario
        if request.method == "POST":
            # Actualizamos el formulario con los datos recibidos
            form = UsuForm(request.POST, instance=instancia)
            # Si el formulario es válido...
            if form.is_valid():
                # Guardamos el formulario pero sin confirmarlo,
                # así conseguiremos una instancia para manejarla
                instancia = form.save(commit=False)
                # Podemos guardarla cuando queramos
                instancia.save()
            messages.info(request,'Usuario Modificado')
            return redirect('UsuarioAdmin')
                # Si llegamos al final renderizamos el formulario
        return render(request, 'TesisApp/registro_admin.html', {'form': form})


    def delete(request, id):
        # Recuperamos la instancia de la persona y la borramos
        instancia = User.objects.get (id=id)
        instancia.delete()
    # Después redireccionamos de nuevo a la lista
        return redirect('UsuarioAdmin')

     

def UsuarioLista(request):
    usuario = User.objects.values()
    return render(request,"TesisApp/usuario_admin.html",{'usuarios':usuario})
     
def Inicio(request):
    return render(request,"TesisApp/Inicio.html")

def Admin(request):       
    return render(request,"TesisApp/admin.html")

def Logout(request):
    logout(request)
    messages.success(request,F"La sesion se ha cerrado")
    return redirect('Login')

def Login(request):
    return render(request,"TesisApp/Login.html")

def ConficUsu(request):
    return render(request,"TesisApp/config_usu.html")

def ModeloReact(request):
    return render(request,"TesisApp/modelo_reactor.html")
  