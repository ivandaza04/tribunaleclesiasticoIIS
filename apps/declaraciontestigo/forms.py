from django import forms

from django.forms import ClearableFileInput
from apps.declaraciontestigo.models import DeclaracionTestigo


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class DeclaracionTestigoForm(forms.ModelForm):
    class Meta:
        model = DeclaracionTestigo

        fields = [
            # 'proceso',
            'nombre',
            'fecha',
            'testigo',
            'observacion',
            'docfile',
        ]
        labels = {
            # 'proceso': 'Proceso',
            'nombre': 'Declaración',
            'fecha': 'Fecha',
            'testigo': 'Testigo',
            'observacion': 'Observación',
            'docfile': 'Documento',
        }
        widgets = {
            # 'proceso': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'testigo': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            'docfile': CustomClearableFileInput,
        }
