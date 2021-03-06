from django.contrib import admin

from condominio.models import Condominio,CuentaCondominio, Vivienda,ViviendaUsuario,Propietario,Perfil,Usuario,CategoriaGastoComun,SubcategoriaGastoComun,Documento, DetalleGastoComun

class PropietariosAdmin(admin.ModelAdmin):
    list_display = ('idPersona','nombres', 'apellido_Paterno', 'apellido_Materno','telefono','correo')
    search_fields=('apellido_Paterno',)
    list_filter=('fecha_Nacimiento',)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombres','apellido_Paterno','telefono','idVivienda','id_Propietario', 'fecha_Creacion','fecha_Modificacion','fecha_Eliminacion','estado_Usuario')
    search_fields=('idUsuario','apellido_Paterno',)
class ViviendaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'idVivienda','observacion','fecha_Creacion')
class SubCategoriaGastoComunAdmin(admin.ModelAdmin):
    list_display = ('idSubcategoria','Descripcion_Subcategoria','idCategoria')
    list_filter=('idCategoria',)
    ordering = ('idSubcategoria',)
    

class DocumentoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos Internos', {'fields' :  ('idDocumento','tipoDoc')}),
        ('Datos Propios del documento', {'fields' : ('numerodoc','montoTotal','fecha_Vencimiento','idCalendario','observacion','fecha_Emision')}),
    )
# Register your models here.


admin.site.register(CuentaCondominio)
admin.site.register(Vivienda)
admin.site.register(ViviendaUsuario, ViviendaUsuarioAdmin)
admin.site.register(Propietario, PropietariosAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(CategoriaGastoComun)
admin.site.register(SubcategoriaGastoComun,SubCategoriaGastoComunAdmin)
admin.site.register(Documento,DocumentoAdmin)
admin.site.register(DetalleGastoComun)
