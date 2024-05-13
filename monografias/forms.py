from django import forms
from .models import Monografia
from equipe.models import Pesquisador, Titulacao


class MonografiaForm(forms.ModelForm):
    banca_examinadora = forms.ModelMultipleChoiceField(
        queryset=Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.DOUTORADO, Titulacao.MESTRADO, Titulacao.MESTRADO]),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Banca Examinadora"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar os campos de autor, orientador e coorientador
        self.fields['autor'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.GRADUANDO, Titulacao.GRADUACAO])
        self.fields['orientador'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.DOUTORADO, Titulacao.MESTRADO, Titulacao.MESTRADO])
        self.fields['coorientador'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.DOUTORADO, Titulacao.MESTRADO, Titulacao.MESTRADO])

    class Meta:
        model = Monografia
        fields = '__all__'
