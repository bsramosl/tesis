from django.shortcuts import render,HttpResponse
from TesisApp.models import Usuario
from django.shortcuts import render,redirect 
from django.contrib import messages
from django.db import connections
import mysql.connector
from operator import itemgetter
from .forms import UsuarioForm

class crud():
        
    def login(request):
        con = mysql.connector.connect(host="localhost",user="root",
        passwd="",database="tesis")
        cursor = con.cursor()
        con2 = mysql.connector.connect(host="localhost",user="root",
        passwd="",database="tesis")
        cursor2 = con2.cursor()
        sqlcommand = "select Usuario from tesisapp_usuario"
        sqlcommand2 = "select Contraseña from tesisapp_usuario"
        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)
        e=[]
        p=[]
       
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p)) 
         
        con3 = mysql.connector.connect(host="localhost",user="root",
        passwd="",database="tesis")
        cursor3 = con2.cursor()

        if request.method =="POST":
            Usuario = request.POST['username']
            Contraseña = request.POST['password']
            k=len(res)
            i=0
            sqlcommand3 = "select Usuario from tesisapp_usuario where Usuario = Usuario"
            cursor3.execute(sqlcommand3)
            lst =[]
            for name in cursor3:
                name = name
                name2 =''.join(name)           
            while i < k:                
                
                if res[i]==Usuario and res2[i]==Contraseña:                    
                   return render(request,'TesisApp/Inicio.html',{'name':Usuario})
                   break
                              
                i=i+1   
                           
            else:   
                          
                messages.info(request,"Check userName or password")
                return redirect('Login')

        return render(request,'TesisApp/login.html')   
        return render(request,'TesisApp/Inicio.html')  

    def add(request):
        # Creamos un formulario vacío
        form = UsuarioForm()
        # Comprobamos si se ha enviado el formulario
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = UsuarioForm(request.POST)
            # Si el formulario es válido...
            if form.is_valid():
                # Guardamos el formulario pero sin confirmarlo,
                # así conseguiremos una instancia para manejarla
                instancia = form.save(commit=False)
                # Podemos guardarla cuando queramos
                instancia.save()
            print (form)
                # Después de guardar redireccionamos a la lista
            return redirect('/')
            # Si llegamos al final renderizamos el formulario
        return render(request, 'TesisApp/registro.html', {'form': form}) 

    def edit(request, id):
        # Recuperamos la instancia de la persona
        instancia = Usuario.objects.get(id=id)
        # Creamos el formulario con los datos de la instancia
        form = UsuarioForm(instance=instancia)
        # Comprobamos si se ha enviado el formulario
        if request.method == "POST":
            # Actualizamos el formulario con los datos recibidos
            form = UsuarioForm(request.POST, instance=instancia)
            # Si el formulario es válido...
            if form.is_valid():
                # Guardamos el formulario pero sin confirmarlo,
                # así conseguiremos una instancia para manejarla
                instancia = form.save(commit=False)
                # Podemos guardarla cuando queramos
                instancia.save()
            messages.info(request,"Usuario Modificado")
            return redirect('UsuarioAdmin')
                # Si llegamos al final renderizamos el formulario
        return render(request, 'TesisApp/registro_admin.html', {'form': form})
    
    def delete(request, id):
        # Recuperamos la instancia de la persona y la borramos
        instancia = Usuario.objects.get(id=id)
        instancia.delete()
    # Después redireccionamos de nuevo a la lista
        return redirect('UsuarioAdmin')
 

def UsuarioLista(request):
    usuario = Usuario.objects.all()
    return render(request,"TesisApp/usuario_admin.html",{'usuarios':usuario})

def admin(request):       
    return render(request,"TesisApp/admin.html")

def inicio(request):       
    return render(request,"TesisApp/Inicio.html")

def busqueda(request):
    return render(request,"TesisApp/busqueda_inicio.html")

def inactivacion(request):   
    return render(request,"TesisApp/Termica.html")

def admin(request):   
    return render(request,"TesisApp/admin.html")
    
def base(request):   
    return render(request,"TesisApp/base_usu.html")

