from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout

def Acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            


class VistaRegistro(View):
    
    def get(self,request):
        form = UserCreationForm()
        return render(request,"TesisApp/registro.html",{"form":form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            messages.success(request,F"Bienvenido {nombre_usuario}")
            login(request, usuario)
            return render(request,"TesisApp/Inicio.html",{"message":nombre_usuario})
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,"TesisApp/registro.html")

def Inicio(request):
    return render(request,"TesisApp/Inicio.html")

def Logout(request):
    logout(request)
    messages.success(request,F"La sesion se ha cerrado")
    return render(request,"TesisApp/Login.html")

def Login(request):
    return render(request,"TesisApp/Login.html")
