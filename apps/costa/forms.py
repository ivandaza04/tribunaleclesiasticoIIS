from django import forms

from apps.costa.models import Costa


class CostaForm(forms.ModelForm):
    class Meta:
        model = Costa

        fields = [
            'proceso',
            'fecha',
            'total',
        ]
        labels = {
            'proceso': 'Nombre del Proceso',
            'fecha': 'Fecha',
            'total': 'Total',
        }
        widgets = {
            'proceso': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
