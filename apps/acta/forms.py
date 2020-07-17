from django import forms

from django.forms import ClearableFileInput
from apps.acta.models import Acta


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class ActaForm(forms.ModelForm):
    class Meta:
        model = Acta

        fields = [
            # 'proceso',
            'fecha',
            'presidente',
            'defensor',
            'juez1',
            'juez2',
            'ponente',
            'veto',
            'canon',
            'consta',
            'docfile',
        ]
        labels = {
            # 'proceso': 'Proceso',
            'fecha': 'Fecha',
            'presidente': 'Presidente',
            'defensor': 'Defensor',
            'juez1': 'Primer Juez',
            'juez2': 'Segundo Juez',
            'ponente': 'Ponente',
            'veto': 'Veto',
            'canon': 'Canon',
            'consta': 'Consta',
            'docfile': 'Documento Adjunto',
        }
        widgets = {
            # 'proceso': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'presidente': forms.Select(attrs={'class': 'form-control'}),
            'defensor': forms.Select(attrs={'class': 'form-control'}),
            'juez1': forms.Select(attrs={'class': 'form-control'}),
            'juez2': forms.Select(attrs={'class': 'form-control'}),
            'ponente': forms.Select(attrs={'class': 'form-control'}),
            'veto': forms.CheckboxSelectMultiple(),
            'canon': forms.CheckboxSelectMultiple(),
            'consta': forms.Textarea(attrs={'class': 'form-control'}),
            'docfile': CustomClearableFileInput,
        }
