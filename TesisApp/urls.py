from django.urls import path
from TesisApp import views

urlpatterns = [
    path('',views.crud.login, name="Login"), #Nombre--vista  --
    path('Login',views.crud.login,name="Login"), 
    path('Inicio',views.inicio, name="Inicio"),
    path('Admin',views.UsuarioLista, name="Admin"),
    path('Termica',views.inactivacion,name="Termica"),
    path('Registro',views.crud.add,name="Registro"),
    path('Crecimiento',views.crecimiento,name = "Crecimiento"),

]