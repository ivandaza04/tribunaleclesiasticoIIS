from django.contrib import admin

# Register your models here.
from apps.declaraciontestigo.models import DeclaracionTestigo, Tipo

admin.site.register(DeclaracionTestigo)
admin.site.register(Tipo)