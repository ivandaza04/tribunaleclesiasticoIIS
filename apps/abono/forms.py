from django import forms

from apps.abono.models import Abono


class AbonoForm(forms.ModelForm):
    class Meta:
        model = Abono

        fields = [
            # 'costa',
            'fecha',
            'valor',
        ]
        labels = {
            # 'costa': 'Nombre del Proceso',
            'fecha': 'Fecha',
            'valor': 'Valor',
        }
        widgets = {
            # 'costa': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }
