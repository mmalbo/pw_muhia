from django import forms
from .models import Solicitud, Servicio

class SolicitudForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Solicitud
        fields = ['usuario', 'telefono', 'correo', 'carnet', 'servicios']
        labels = {'carnet':'Carnet de identidad', 'usuario':'Nombre y apellidos'
                  , 'telefono':'Teléfono', 'correo':'Correo electrónico'}
        