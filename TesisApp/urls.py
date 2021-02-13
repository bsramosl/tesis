from django.urls import path
from TesisApp import views

urlpatterns = [
    path('',views.LoginAndRegister.login, name="Login"), #Nombre--vista  --
    path('Login',views.LoginAndRegister.login,name="Login"), 
    path('Inicio',views.inicio, name="Inicio"),
    path('Admin',views.TablasListadas.UsuarioLista, name="Admin"),
    path('Termica',views.inactivacion,name="Termica"),
    path('Registro',views.LoginAndRegister.register,name="Registro"),
    path('Crecimiento',views.crecimiento,name = "Crecimiento"),

]