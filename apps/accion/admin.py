from django.contrib import admin

# Register your models here.
from apps.accion.models import Accion,Tipo

admin.site.register(Accion)
admin.site.register(Tipo)
