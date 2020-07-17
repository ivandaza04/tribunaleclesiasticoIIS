from django.db import models

# Create your models here.
from apps.proceso.models import Proceso
from django.utils import timezone


class Costa(models.Model):
    proceso = models.OneToOneField(
        Proceso, on_delete=models.CASCADE, primary_key=True)
    fecha = models.DateField(default=timezone.now)
    abonado = models.DecimalField(
        max_digits=19, decimal_places=2, null=True, blank=True)
    deuda = models.DecimalField(
        max_digits=19, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(
        max_digits=19, decimal_places=2, null=False, blank=False)
    active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.proceso)
