from django import forms

from django.forms import ClearableFileInput
from apps.sentencia.models import Sentencia


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class SentenciaForm(forms.ModelForm):
    class Meta:
        model = Sentencia

        fields = [
            # 'proceso',
            'fecha',
            'ponente',
            'docfile',
        ]
        labels = {
            # 'proceso': 'Proceso',
            'fecha': 'Fecha',
            'ponente': 'Ponente',
            'docfile': 'Documento',
        }
        widgets = {
            # 'proceso': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'ponente': forms.Select(attrs={'class': 'form-control'}),
            'docfile': CustomClearableFileInput,
        }
