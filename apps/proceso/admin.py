from django.contrib import admin

# Register your models here.
from apps.proceso.models import Tipo,Proceso,Diocesi

admin.site.register(Proceso)
admin.site.register(Tipo)
admin.site.register(Diocesi)
