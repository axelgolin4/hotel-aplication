from dataclasses import fields
from django import forms
from django.forms import ModelForm

from .models import Blancos, Insumos, Cocina

class InsumosForm(ModelForm):
    class Meta:
        model = Insumos
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget(attrs={'class':'fechaentrada'}),
        }

class CocinaForm(ModelForm):
    class Meta:
        model = Cocina
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget(attrs={'class':'fechaentrada'}),
        }

class BlancosForm(ModelForm):
    class Meta:
        model = Blancos
        fields = '__all__'

        widgets = {
            "fecha": forms.SelectDateWidget(attrs={'class':'fechaentrada'}),
        }