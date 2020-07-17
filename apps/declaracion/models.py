from django.db import models

# Create your models here.
from django.utils import timezone
from apps.proceso.models import Proceso


class Tipo(models.Model):
    tipo = models.CharField(unique=True, null=False,
                            blank=False, max_length=100)

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return str(self.tipo)


class Declaracion(models.Model):
    proceso = models.ForeignKey(
        Proceso, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.ForeignKey(
        Tipo, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    observacion = models.TextField(max_length=500, blank=True, null=True)
    docfile = models.FileField(
        blank=True, null=True, upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return str(self.nombre)
