from django import forms

from django.forms import ClearableFileInput
from apps.decreto.models import Decreto


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class DecretoForm(forms.ModelForm):
    class Meta:
        model = Decreto

        fields = [
            # 'proceso',
            'nombre',
            'fecha',
            'docfile',
        ]
        labels = {
            # 'proceso': 'Proceso',
            'nombre': 'Decreto',
            'fecha': 'Fecha',
            'docfile': 'Documento',
        }
        widgets = {
            # 'proceso': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'docfile': CustomClearableFileInput,
        }
