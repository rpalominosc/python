from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos


# Create your views here.

def  busqueda_productos(request):

        return render(request, "busqueda_productos.html" )

def  buscar(request):

    #mensaje = "Articulo buscado: %r"  %request.GET["prod"]
    #producto=request.GET['acme']
    articulos=Articulos.objects.filter(nombre_icontains=producto)

    return render(request, "resultadosbusqueda.html", {"articulos":articulos,"query":producto})

    return HttpResponse(mensaje)
