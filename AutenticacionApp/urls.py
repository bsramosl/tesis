from django.urls import path
from AutenticacionApp import views

urlpatterns = [
    path('',views.Acceder,name="Acceder"),
    path('Registro',views.Registro, name="Registro"),  
    path('Login',views.Acceder, name="Login"), 
    path('Inicio',views.Inicio, name="Inicio"),   
    path('Salir',views.Logout,name="Salir"), 
    path('ConficUsu',views.ConficUsu,name="ConficUsu"),
    
]