from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido= apellido


def saludo (request):

    p1=(Persona("Claudia", "Jelvez"))
    #nombre= "Rodri"
    #apellido="Palominos"

    temas_del_curso=["Plantillas", "Modelos","Bucles","Variables"]
    ahora=datetime.datetime.now()
    #doc_externo=open("/home/spider/github/python/CursoDjango/Proyecto1/Proyecto1/plantillas/platillasaludo.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template('platillasaludo.html')
    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"Hora_actual":ahora, "Temas":temas_del_curso})
    # documento=plt.render(ctx)
    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"Hora_actual":ahora, "Temas":temas_del_curso})

    #return HttpResponse(documento)
    return render(request,'platillasaludo.html', {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido,"Hora_actual":ahora, "Temas":temas_del_curso})

def  despedida(request):
    return HttpResponse("Saliendo del programa")

def cursoc(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "CursoC.html", {"damefecha":fecha_actual})

def cursocss(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "cursocss.html", {"damefecha":fecha_actual})


def damefecha(request):
    fecha_actual=datetime.datetime.day()
    documento=""" <html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return  HttpResponse(documento)

def calculaedad(request,edad,agno):
    #edadactual= 59
    periodo=agno -2019
    edadfutura= edad+periodo
    documento=""" <html>
    <body>
    <h2>
    En el año  %s tendrás %s años
    </h2>
    </body>
    </html>""" %(agno,edadfutura)
    return HttpResponse(documento)
