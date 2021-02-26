from django.urls import path
from AutenticacionApp import views

urlpatterns = [
    path('',views.Acceder,name="Acceder"),
    path('Registro',views.Registro, name="Registro"),  
    path('Login',views.Acceder, name="Login"), 
    path('Inicio',views.Inicio, name="Inicio"),   
    path('Salir',views.Logout,name="Salir"), 
    path('ConficUsu',views.cambiar_contraseña,name="ConficUsu"),
    path('UsuarioAdmin',views.UsuarioLista, name="UsuarioAdmin"),
    path('ModeloReact',views.ModeloReact, name="ModeloReact"),
    path('Admin',views.Admin, name="Admin"),
    path('edit/<int:id>',views.Crud.edit,),  
    path('delete/<int:id>',views.Crud.delete),
     
    
]