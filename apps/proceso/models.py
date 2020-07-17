from django.db import models

# Create your models here.
from django.utils import timezone
from apps.colegiado.models import Colegiado
from apps.persona.models import Persona


class Tipo(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return str(self.nombre)


class Diocesi(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Proceso(models.Model):
    radicado = models.IntegerField(
        primary_key=True, null=False, blank=False)
    expediente = models.CharField(
        max_length=50, null=False, blank=False, default=None)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    fecha = models.DateField(default=timezone.now)
    presidente = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE, related_name='person1')
    defensor = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE, related_name='person2')
    juez1 = models.ForeignKey(Colegiado, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='person3')
    juez2 = models.ForeignKey(Colegiado, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='person4')
    demandante = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.CASCADE, related_name='person5')
    demandado = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.CASCADE, related_name='person6')
    notario = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE, related_name='person7')
    observacion = models.TextField(max_length=500, blank=True, null=True)
    tipo = models.ForeignKey(
        Tipo, null=True, blank=True, on_delete=models.CASCADE)
    diocesis = models.ForeignKey(
        Diocesi, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.nombre)
