from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields=('Creado','Actualizado')

admin.site.register(Usuario,UsuarioAdmin)