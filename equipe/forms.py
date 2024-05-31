from django import forms
from .models import Pesquisador
from django.contrib.auth.forms import UserCreationForm


class PesquisadorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Pesquisador
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pesquisador.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email
