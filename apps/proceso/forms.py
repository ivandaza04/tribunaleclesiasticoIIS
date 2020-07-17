from django import forms

from django.forms import ClearableFileInput
from apps.proceso.models import Proceso


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso

        fields = [
            'radicado',
            'expediente',
            'nombre',
            'tipo',
            'diocesis',
            'fecha',
            'presidente',
            'defensor',
            'juez1',
            'juez2',
            'notario',
            'demandante',
            'demandado',
            'observacion',
        ]
        labels = {
            'radicado': 'Número del Radicado',
            'expediente': 'Expediente',
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'fecha': 'Fecha',
            'diocesis': 'Diócesis',
            'presidente': 'Presidente',
            'defensor': 'Defensor del vínculo',
            'juez1': 'Primer Juez',
            'juez2': 'Segundo Juez',
            'notario': 'Notario Eclesiástico',
            'demandante': 'Demandante',
            'demandado': 'Demandado',
            'observacion': 'Observaciones',
        }
        widgets = {
            'radicado': forms.NumberInput(attrs={'class': 'form-control'}),
            'expediente': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'diocesis': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.SelectDateWidget(attrs={'class': 'form-control'}, years=range(2000, 2050)),
            'presidente': forms.Select(attrs={'class': 'form-control'}),
            'defensor': forms.Select(attrs={'class': 'form-control'}),
            'juez1': forms.Select(attrs={'class': 'form-control'}),
            'juez2': forms.Select(attrs={'class': 'form-control'}),
            'notario': forms.Select(attrs={'class': 'form-control'}),
            'demandante': forms.Select(attrs={'class': 'form-control'}),
            'demandado': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }
