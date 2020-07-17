from django.contrib import admin

# Register your models here.
from apps.declaracion.models import Declaracion, Tipo

admin.site.register(Declaracion)
admin.site.register(Tipo)