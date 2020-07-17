from django import forms

from apps.persona.models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'documento',
            'nombre',
            'apellido',
            'direccion',
            'telefono',
            'ciudad',
            'email',
        ]
        labels = {
            'documento': 'Número de documento de identidad',
            'nombre': 'Nombre(s)',
            'apellido': 'Apellido(s)',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'ciudad': 'Ciudad',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }