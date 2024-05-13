from django import forms
from .models import Pesquisador


class PesquisadorForm(forms.ModelForm):
    class Meta:
        model = Pesquisador
        fields = '__all__'
