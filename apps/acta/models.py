from django.db import models

# Create your models here.
from django.utils import timezone
from apps.colegiado.models import Colegiado
from apps.proceso.models import Proceso


class Canon(models.Model):
    idcanon = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.idcanon)


class Veto(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return str(self.nombre)


class Acta(models.Model):
    proceso = models.OneToOneField(
        Proceso, on_delete=models.CASCADE, primary_key=True)
    nombre = models.TextField(default="ACTA DE SESIÓN DE FALLO")
    fecha = models.DateField(default=timezone.now)
    presidente = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE, related_name='person9')
    defensor = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE, related_name='person10')
    juez1 = models.ForeignKey(Colegiado, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='person11')
    juez2 = models.ForeignKey(Colegiado, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='person12')
    ponente = models.ForeignKey(
        Colegiado, null=True, blank=True, on_delete=models.CASCADE, related_name='person13')
    veto = models.ManyToManyField(Veto, blank=True)
    canon = models.ManyToManyField(Canon, blank=True)
    consta = models.TextField(max_length=500, null=True, blank=True)
    docfile = models.FileField(
        blank=True, null=True, upload_to='documents/%Y/%m/%d')

    class Meta:
        ordering = ["-fecha"]
