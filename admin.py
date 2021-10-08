from django.contrib import admin

# Register your models here.
from .models import Identificacion, Grados, Departamento, Estado

#admin.site.register(Identificacion)
#admin.site.register(Grados)
#admin.site.register(Departamento)
#admin.site.register(Estado)

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('id', 'descripcion')
    
@admin.register(Grados)
class GradosAdmin(admin.ModelAdmin):
    list_display=('id', 'descgrado')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display=('id', 'estado')

@admin.register(Identificacion)
class IdentificacionAdmin(admin.ModelAdmin):
    list_display=('id','nombreapellido', 'codigofun', 'cua',  'grados')
        