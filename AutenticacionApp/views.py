from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from  .forms import UsuarioForm, LoginForm ,ContraseñaForm, EditarForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

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

def cambiar_contraseña(request):
    if request.method == 'POST':
        form = ContraseñaForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña ha sido cambiada.')
            return redirect('Inicio')
        else:
            messages.error(request, 'Corrija el error a continuación.')
    else:
        form = ContraseñaForm(request.user)
    return render(request, "TesisApp/config_usu.html", {'form': form})

class Crud():

    def edit(request,id):
        instancia = User.objects.get(id=id)        
        form = UserChangeForm(instance=instancia)
        if request.method == 'POST':
            form = UserChangeForm(request.POST, instance=instancia)
            if form.is_valid():
                form.save()
                instancia.save()
                return redirect('UsuarioAdmin')
        else:
            form = UserChangeForm(instance=instancia)
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