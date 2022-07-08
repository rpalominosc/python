from telnetlib import STATUS
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Identificacion, Departamento, Grados, Estado
# Create your views here.
from CuaApp.forms import GeneraCua

def index(request):
    num_funcionarios=Identificacion.objects.all().count()
    num_activos=Identificacion.objects.filter(estado__exact=1).count()

    return render (request, 'index.html', context={'num_funcionarios':num_funcionarios,'num_activos':num_activos})



def AgregaCua (request):
    
    if request.method == "POST":
        miformulario = GeneraCua(request.POST)

        if miformulario.is_valid():
            infForm = miformulario.cleaned_data['codigofun']
        #    def 

            print (infForm['nombreapellido'], infForm['codigofun'])
            return render (request, "gracias.html")
    else:
        miformulario = GeneraCua()
    
    return render (request, "identificac.html", {'form':miformulario})

#        model = Identificacion
#        fields = '__all__'

    
