from django.contrib import admin

# Register your models here.
from apps.citacion.models import Citacion, Tipo

admin.site.register(Citacion)
admin.site.register(Tipo)
