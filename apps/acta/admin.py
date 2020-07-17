from django.contrib import admin

# Register your models here.
from apps.acta.models import Acta,Canon, Veto

admin.site.register(Acta)
admin.site.register(Canon)
admin.site.register(Veto)
