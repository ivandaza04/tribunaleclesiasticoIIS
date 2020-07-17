from django import forms

from apps.home.models import Entrada


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada

        fields = [
            'titulo',
            'fecha',
            'observacion'
        ]
        labels = {
            'titulo': 'titulo',
            'fecha': 'Fecha',
            'observacion': 'Observaciones',
        }
