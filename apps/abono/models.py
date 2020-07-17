from django.db import models

# Create your models here.
from apps.costa.models import Costa
from django.utils import timezone


class Abono(models.Model):
    costa = models.ForeignKey(
        Costa, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    valor = models.DecimalField(
        max_digits=19, decimal_places=2, null=False, blank=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.valor)
