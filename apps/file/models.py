from django.db import models

# Create your models here.
from django.utils import timezone
from apps.proceso.models import Proceso


class File(models.Model):
    proceso = models.ForeignKey(
        Proceso, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    fecha = models.DateTimeField(default=timezone.now)
    docfile = models.FileField(
        null=True, blank=True, upload_to='documents/%Y/%m/%d')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.fecha = timezone.now()
        return super().save(force_insert=force_insert, force_update=force_update,
                            using=using, update_fields=update_fields)

    def __str__(self):
        return self.nombre
