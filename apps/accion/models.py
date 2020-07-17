from django.db import models

# Create your models here.
from apps.proceso.models import Proceso
from django.utils import timezone


class Tipo(models.Model):
    tipo = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return str(self.tipo)


class Accion(models.Model):
    proceso = models.ForeignKey(
        Proceso, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.ForeignKey(
        Tipo, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    observacion = models.TextField(max_length=500, blank=True, null=True)
    docfile = models.FileField(
        blank=True, null=True, upload_to='documents/%Y/%m/%d')

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.nombre)
