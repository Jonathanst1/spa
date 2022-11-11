from django import forms
from .models import plano

class PlanoModelForm(forms.ModelForm):
    class Meta:
        model = plano
        fields = '__all__'