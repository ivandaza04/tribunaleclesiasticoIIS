from django import forms

from django.forms import ClearableFileInput
from apps.citacion.models import Citacion

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class CitacionForm(forms.ModelForm):
    class Meta:
        model = Citacion

        fields = [
            # 'proceso',
            'nombre',
            'fecha',
            'citado',
            'citacion',
            'hora',
            'numero',
            'docfile',
        ]
        labels = {
            # 'proceso': 'Proceso',
            'nombre': 'Finalidad',
            'fecha': 'Fecha',
            'citado': 'Citado',
            'citacion': 'Fecha de la Citación',
            'hora': 'Hora de la Citación (HORA:MINUTO) AM/PM',
            'numero': 'Numero de la citación',
            'docfile': 'Documento',
        }
        widgets = {
            # 'proceso': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'citado': forms.Select(attrs={'class': 'form-control'}),
            'citacion': forms.SelectDateWidget(attrs={'class': 'form-control'},years=range(2000, 2030)),
            'hora': forms.TimeInput(attrs={'class': 'form-control'},format='%I:%M %p'),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'docfile': CustomClearableFileInput,
        }