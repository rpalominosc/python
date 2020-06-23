from django.contrib import admin

from condominio.models import Condominio,CuentaCondominio, Vivienda,ViviendaUsuario,Persona,Perfil,Usuario

class PersonasAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_Paterno', 'apellido_Materno','fecha_Nacimiento')
    search_fields=('apellido_Paterno',)
    list_filter=('fecha_Nacimiento',)


# Register your models here.

admin.site.register(Condominio)
admin.site.register(CuentaCondominio)
admin.site.register(Vivienda)
admin.site.register(ViviendaUsuario)
admin.site.register(Persona, PersonasAdmin)
admin.site.register(Perfil)
admin.site.register(Usuario)
