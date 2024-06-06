from django import forms
from .models import Monografia
from equipe.models import Pesquisador, Titulacao


from django import forms
from .models import Monografia
from equipe.models import Pesquisador

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
        self.fields['autor'].queryset = Pesquisador.objects.filter(
            nivel=Titulacao.GRADUACAO
        ).exclude(
            id__in=Monografia.objects.values('autor_id')  
        )
        self.fields['orientador'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.DOUTORADO, Titulacao.MESTRADO, Titulacao.MESTRADO])
        self.fields['coorientador'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.DOUTORADO, Titulacao.MESTRADO, Titulacao.MESTRADO])

    class Meta:
        model = Monografia
        fields = '__all__'



class AlunoMonografiaForm(forms.ModelForm):
    banca_examinadora = forms.ModelMultipleChoiceField(
        queryset=Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.MESTRADO]),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Banca Examinadora"
    )

    class Meta:
        model = Monografia
        fields = ['titulo', 'resumo', 'orientador', 'coorientador', 'banca_examinadora', 'palavras_chave','area_concentracao', 'arquivos']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['autor'] = forms.ModelChoiceField(
                queryset=Pesquisador.objects.filter(id=user.id),
                initial=user,
                widget=forms.HiddenInput()
            )
        self.fields['orientador'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.MESTRADO])
        self.fields['coorientador'].queryset = Pesquisador.objects.filter(
            nivel__in=[Titulacao.DOUTORADO, Titulacao.MESTRADO])