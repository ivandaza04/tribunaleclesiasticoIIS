from django.contrib import admin

# Register your models here.
from apps.ciudad.models import Ciudad, Departamento

admin.site.register(Ciudad)
admin.site.register(Departamento)