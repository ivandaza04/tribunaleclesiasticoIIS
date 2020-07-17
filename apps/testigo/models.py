from django.db import models
from apps.ciudad.models import Ciudad

# Create your models here.


class Testigo(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=70, null=False, blank=False)
    direccion = models.CharField(
        max_length=50, blank=True, null=True, default=None)
    telefono = models.CharField(
        max_length=12, blank=True, null=True, default=None)
    ciudad = models.ForeignKey(
        Ciudad, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True, default=None)
    active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre+" "+self.apellido+" , "+str(self.ciudad)
