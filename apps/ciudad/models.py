from django.db import models

# Create your models here.


class Departamento(models.Model):
    departamento = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    class Meta:
        ordering = ["departamento"]

    def __str__(self):
        return self.departamento


class Ciudad(models.Model):
    ciudad = models.CharField(
        max_length=50, null=False, blank=False)
    departamento = models.ForeignKey(
        Departamento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["departamento"]

    def __str__(self):
        return self.ciudad+" - "+str(self.departamento)
