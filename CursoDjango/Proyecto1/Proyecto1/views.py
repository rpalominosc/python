from django.http import HttpResponse

def saludo (request):
    return HttpResponse("Hola Giles, esta es la primera página creada con Django")

def  despedida(request):
    return HttpResponse("Saliendo del programa")
