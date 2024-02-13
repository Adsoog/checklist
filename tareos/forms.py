from django import forms
from .models import Persona, DesempenoDiario

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre']

class DesempenoForm(forms.ModelForm):
    class Meta:
        model = DesempenoDiario
        fields = '__all__'

class DesempenoEditForm(forms.ModelForm):
    class Meta:
        model = DesempenoDiario
        fields = ['puntuacion']

    puntuacion = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1, 'max': 10})
    )