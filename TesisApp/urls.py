from django.urls import path
from TesisApp import views

urlpatterns = [
    path('',views.crud.login, name="Login"), #Nombre--vista  --
    path('Login',views.crud.login,name="Login"), 
    path('Base',views.base,name="Base"),
    path('Inicio',views.inicio, name="Inicio"),
    path('UsuarioAdmin',views.UsuarioLista, name="UsuarioAdmin"),
    path('Admin',views.admin, name="Admin"),
    path('Editar',views.crud.edit,name="Editar"),
    path('edit/<int:id>',views.crud.edit),
    path('delete/<int:id>',views.crud.delete),    
    path('Registro',views.crud.add,name="Registro"),
    path('Busqueda',views.busqueda,name = "Busqueda"),

]