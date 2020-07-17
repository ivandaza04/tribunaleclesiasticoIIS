from django.db import models

# Create your models here.
from django.utils import timezone
from apps.proceso.models import Proceso
from apps.colegiado.models import Colegiado


class Sentencia(models.Model):
    proceso = models.OneToOneField(
        Proceso, on_delete=models.CASCADE, primary_key=True)
    nombre = models.TextField(default="SENTENCIA DEL PROCESO")
    ponente = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    docfile = models.FileField(
        blank=True, null=True, upload_to='documents/%Y/%m/%d')
