from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome')
    password = forms.CharField(label='Senha')
