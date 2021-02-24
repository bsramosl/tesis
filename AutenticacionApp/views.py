from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm



class VistaRegistro(View):
    
    def get(self,request):
        form = UserCreationForm()
        return render(request,"TesisApp/registro.html",{'form':form})

    def post(self,render):
        return
