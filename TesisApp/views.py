from django.shortcuts import render,HttpResponse
from TesisApp.models import Usuario
from django.shortcuts import render,redirect 
from django.contrib import messages
from django.db import connections
import mysql.connector
from operator import itemgetter

class LoginAndRegister():
    
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
            sqlcommand3 = "select Nombre from tesisapp_usuario where Usuario = Usuario"
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


    def register(request):        
        if request.method =="POST":
            usuario = Usuario ()            
            usuario.Usuario = request.POST['username']
            usuario.Nombre = request.POST['Nombre']
            usuario.Apellido = request.POST['Apellido']            
            usuario.Email = request.POST['Email']
            usuario.Contraseña = request.POST['password']
            usuario.ReContraseña = request.POST['repassword']
            if usuario.Contraseña!=usuario.ReContraseña:
                messages.info(request,"Passwords not match")
                return redirect('Registro')  
            elif usuario.Nombre=="" or usuario.Apellido=="" or usuario.Email=="" or usuario.Contraseña =="" or usuario.ReContraseña=="":
                messages.info(request,"Some fields are missing")
                return redirect('Registro')   
            else:
                messages.info(request,"Registro realizado")
                usuario.save()
            
            return render(request,'TesisApp/login.html')   
        else:
            return render(request,'TesisApp/registro.html')   
            
        return render(request,'TesisApp/registro.html')    

class TablasListadas():
    def UsuarioLista(request):
        usuario = Usuario.objects.all()
        return render(request,"TesisApp/admin.html",{'usuarios':usuario})

def admin(request):       
    return render(request,"TesisApp/admin.html")

def inicio(request):       
    return render(request,"TesisApp/Inicio.html")

def crecimiento(request):
    usuarios=Usuario.objects.all()
    return render(request,"TesisApp/Crecimiento.html",{"usuarios":usuarios})

def inactivacion(request):
    return render(request,"TesisApp/Termica.html")

