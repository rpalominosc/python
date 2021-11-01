from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from CuaApp.forms import GeneraCua

def AgregaCua (request):

    if request.method == "POST":
        miformulario = GeneraCua(request.POST)

        if miformulario.is_valid():
            infForm = miformulario.cleaned_data
        #    def 

            print (infForm['nombreapellido'], infForm['codigofun'])
            return render (request, "gracias.html")
    else:
        miformulario = GeneraCua()
    
    return render (request, "identificac.html", {"form":miformulario})

#        model = Identificacion
#        fields = '__all__'

    
