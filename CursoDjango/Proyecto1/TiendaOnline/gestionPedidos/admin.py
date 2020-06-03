from django.contrib import admin
from gestionPedidos.models import Clientes, Pedidos,Articulos

class ClientesAdmin(admin.ModelAdmin):
        list_display=("nombre","telefono")
        search_fields=("nombre", "telefono")
class ArticulosAdmin(admin.ModelAdmin):
        list_display=("nombre","seccion","precio")
        #search_fields=("nombre", "seccion")
        list_filter=("seccion",)
class PedidosAdmin(admin.ModelAdmin):
        list_display=("numero","fecha","entregado")
        #search_fields=("nombre", "seccion")
        list_filter=("entregado",)
        date_hierarchy="fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Pedidos,PedidosAdmin)
admin.site.register(Articulos,ArticulosAdmin)

# Register your models here.
