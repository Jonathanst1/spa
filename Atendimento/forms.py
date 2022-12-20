from django import forms
from .models import plano


class PlanoModelForm(forms.ModelForm):
    class Meta:
        model = plano
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)

    