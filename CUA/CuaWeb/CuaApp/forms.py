from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from CuaApp.models import Identificacion, Grados,Departamento,Estado

class GeneraCua(ModelForm):
    
    class Meta:
        model = Identificacion
        fields = ['codigofun','nombreapellido','grado','departamento','estado']
        labels = {'nombreapellido':'Nombre', 'codigofun':'Codigo Funcionario' }
    #    help_texts = {'nombreapellido': 'Ingrese APELLIDOS + NOMBRES'}
