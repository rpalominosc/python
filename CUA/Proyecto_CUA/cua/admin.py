from django.contrib import admin

# Register your models here.
from .models import Identificacion, Grados, Departamento, Estado

admin.site.register(Identificacion)
admin.site.register(Grados)
admin.site.register(Departamento)
admin.site.register(Estado)