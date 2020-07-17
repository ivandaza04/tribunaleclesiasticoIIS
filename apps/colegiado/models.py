from django.db import models
from apps.ciudad.models import Ciudad

# Create your models here.


class Colegiado(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.ForeignKey(
        Ciudad, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.nombre)
