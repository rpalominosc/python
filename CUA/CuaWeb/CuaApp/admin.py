from django.contrib import admin
from CuaApp.models import Identificacion, Grados,Departamento,Estado

# Register your models here.

#admin.site.register(Identificacion)
#admin.site.register(Departamento)
#admin.site.register(Grados)
#admin.site.register(Estado)

class IdentificacionAdmin(admin.ModelAdmin):
    list_display = ('nombreapellido','codigofun', 'cua', 'departamento', 'grado','estado')
    #list_filter = ('codigofun', 'cua', 'departamento', 'grado', 'estado')
    ordering = ('codigofun',)
    search_fields = ('nombreapellido', 'codigofun', 'cua',)
    
        
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    ordering = ('id',)
    
class GradosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descgrado')
    

class EstadoAdmin(admin.ModelAdmin):
    list_display= ('id' , 'estado')

admin.site.register(Identificacion,IdentificacionAdmin)
admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Grados, GradosAdmin)
admin.site.register(Estado, EstadoAdmin)