from django.contrib import admin
from CuaApp.models import Identificacion,Grados,Departamento,Estado

# Register your models here.

#admin.site.register(Identificacion)
#admin.site.register(Departamento)
#admin.site.register(Grados)
#admin.site.register(Estado)

admin.site.site_header = 'DIPOLCAR'
admin.site.index_title = 'Administración C.U.A'
admin.site.site_title = 'C.U.A - Dipolcar'
admin.ModelAdmin.actions_on_top = False
admin.site.empty_value_display = '(NO encontrado)'


class IdentificacionAdmin(admin.ModelAdmin):
    list_display = ['nombreapellido','codigofun', 'cua', 'departamento', 'grado', 'estado',]
    search_fields = ('nombreapellido', 'codigofun', 'cua', )
    
        
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion',)
    def __str__(self):
        return self.descripcion
    
class GradosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descgrado',)
           

class EstadoAdmin(admin.ModelAdmin):
    list_display= ('id' , 'estado')

# @admin.display(ordering='identificacion__estado')
class IdentDept(admin.ModelAdmin):
    #model = Identificacion
    list_display = [ 'nombreapellido','codigofun','cua','trae_grado','trae_dep','trae_estado',]
    search_fields = ('nombreapellido', 'codigofun', 'cua', )
    list_per_page = 20
    
    list_filter = ['estado','grado']
    readonly_fields = ['codigofun', 'cua',]
    
#    @admin.display(description='Estado')
    def trae_estado(self,obj):
        return obj.estado.estado

#    @admin.display(description='Departamento')    
    def trae_dep(self,obj):
        return obj.departamento.descripcion
    
#    @admin.display(description='Grado')
    def trae_grado(self,obj):
        return obj.grado.descgrado
    
 
#admin.site.register(Identificacion,IdentificacionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Grados, GradosAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Identificacion,IdentDept)