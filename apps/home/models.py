from django.db import models

# Create your models here.
from django.utils import timezone

from ckeditor.fields import RichTextField


class Entrada(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    fecha = models.DateField(default=timezone.now)
    contenido = RichTextField(blank=True, null=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.titulo)
