from django import forms

from apps.testigo.models import Testigo


class TestigoForm(forms.ModelForm):
    class Meta:
        model = Testigo

        fields = [
            'nombre',
            'apellido',
            'direccion',
            'telefono',
            'ciudad',
            'email',
        ]
        labels = {
            'nombre': 'Nombre(s)',
            'apellido': 'Apellido(s)',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'ciudad': 'Ciudad',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
