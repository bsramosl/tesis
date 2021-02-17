from django.db import models

rol=[(1,'Admin'),(2,'Usuario')]



class Usuario(models.Model):
    Usuario = models.CharField(max_length=50)
    Nombre  = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    ReContraseña = models.CharField(max_length=50)
    Rol = models.IntegerField(choices=rol)
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now_add=True)   


    class Meta:
        verbose_name='usuario'
        verbose_name_plural ='usuarios'

    def __str__(self):
        return self.Usuario
        return self.Nombre
        return self.Apellido
