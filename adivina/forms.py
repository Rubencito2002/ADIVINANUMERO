from django import forms
from .models import adivina

class adivinaForm(forms.ModelForm):
    class Meta:
        model = adivina
        fields = ['number_secret', 'attempts']