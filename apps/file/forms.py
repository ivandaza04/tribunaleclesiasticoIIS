from django import forms

from django.forms import ClearableFileInput
from apps.file.models import File


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class FileForm(forms.ModelForm):
    class Meta:
        model = File

        fields = [
            'proceso',
            'nombre',
            'docfile',
        ]
        labels = {
            'proceso': 'Proceso',
            'nombre': 'Nombre',
            'docfile': 'Documento',
        }
        widgets = {
            'proceso': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'docfile': CustomClearableFileInput,
        }
