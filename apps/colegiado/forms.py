from django import forms

from apps.colegiado.models import Colegiado


class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Colegiado

        fields = [
            'nombre',
            'ciudad',
        ]
        labels = {
            'nombre': 'Nombre(s) y Apellido(s)',
            'ciudad': 'Ciudad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
        }
