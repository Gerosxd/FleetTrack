# flota/forms.py
from django import forms
from .models import Camion

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CamionForm, self).__init__(*args, **kwargs)
        # Bucle para añadir la clase 'form-control' a todos los campos
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-control'})