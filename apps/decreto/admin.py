from django.contrib import admin

# Register your models here.
from apps.decreto.models import Decreto,Tipo

admin.site.register(Decreto)
admin.site.register(Tipo)
