from django.db import models

# Create your models here.
from django.utils import timezone
from apps.persona.models import Persona
from apps.proceso.models import Proceso


class Tipo(models.Model):
    tipo = models.CharField(
        max_length=100, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["tipo"]

    def __str__(self):
        return str(self.tipo)


class Citacion(models.Model):
    proceso = models.ForeignKey(
        Proceso, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.ForeignKey(
        Tipo, null=False, blank=False, on_delete=models.CASCADE)
    citado = models.ForeignKey(
        Persona, null=False, blank=False, on_delete=models.CASCADE, related_name='person1')
    fecha = models.DateField(default=timezone.now)
    citacion = models.DateField(default=timezone.now, null=True, blank=True)
    hora = models.TimeField(default=timezone.now, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    docfile = models.FileField(
        blank=True, null=True, upload_to='documents/%Y/%m/%d')

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.nombre)
