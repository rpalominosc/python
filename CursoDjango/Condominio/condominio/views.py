from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return HttpResponse("Bienvenidos a la pagina indice de Condominios")

# Create your views here.
