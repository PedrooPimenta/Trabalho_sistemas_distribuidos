from django import forms
from .models import Monografia
from equipe.models import Pesquisador


class MonografiaForm(forms.ModelForm):
    banca_examinadora = forms.ModelMultipleChoiceField(
        queryset=Pesquisador.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Banca Examinadora"
    )

    class Meta:
        model = Monografia
        fields = '__all__'
