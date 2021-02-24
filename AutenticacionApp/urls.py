from django.urls import path
from AutenticacionApp import views

urlpatterns = [
    path('',views.Login,name="Login"),
    path('Registro',views.VistaRegistro.as_view(), name="Registro"),  
    path('Inicio',views.Inicio, name="Inicio"),   
    path('Salir',views.Logout,name="Salir")   
]