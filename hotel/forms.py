from dataclasses import fields
from django import forms
from django.forms import ModelForm

from .models import Insumos

class InsumosForm(ModelForm):
    class Meta:
        model = Insumos
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget(attrs={'class':'fechaentrada'}),
        }

