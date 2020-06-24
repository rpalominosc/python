from django.contrib import admin

from condominio.models import Condominio,CuentaCondominio, Vivienda,ViviendaUsuario,Propietario,Perfil,Usuario

class PropietariosAdmin(admin.ModelAdmin):
    list_display = ('idPersona','nombres', 'apellido_Paterno', 'apellido_Materno','telefono','correo')
    search_fields=('apellido_Paterno',)
    list_filter=('fecha_Nacimiento',)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombres','apellido_Paterno','telefono','id_Propietario','estado_Usuario', 'fecha_Creacion','fecha_Modificacion','fecha_Eliminacion')

class ViviendaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'idVivienda','observacion','fecha_Creacion')


# Register your models here.

admin.site.register(Condominio)
admin.site.register(CuentaCondominio)
admin.site.register(Vivienda)
admin.site.register(ViviendaUsuario, ViviendaUsuarioAdmin)
admin.site.register(Propietario, PropietariosAdmin)
admin.site.register(Perfil)
admin.site.register(Usuario, UsuariosAdmin)
