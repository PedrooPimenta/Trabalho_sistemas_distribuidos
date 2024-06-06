from django import forms
from .models import Pesquisador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class PesquisadorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Pesquisador
        fields = ['username', 'email', 'password1', 'password2',
                  'lattes', 'linkedin', 'researchgate', 'nivel', 'cargo']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pesquisador.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email


class AlunoForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Pesquisador
        fields = ['username', 'email', 'password1', 'password2',
                  'lattes', 'linkedin', 'researchgate']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pesquisador.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.cargo = 'Aluno'
        user.nivel = 'Graduação'
        if commit:
            user.save()
            grupo_aluno = Group.objects.get(name='Aluno')
            user.groups.add(grupo_aluno)
        return user

class ProfessorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Pesquisador
        fields = ['username', 'email', 'password1', 'password2',
                  'lattes', 'linkedin', 'researchgate', 'nivel']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pesquisador.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.cargo = 'Professor'
        if commit:
            user.save()
            grupo_professor = Group.objects.get(name='Professor')
            user.groups.add(grupo_professor)
        return user
    
class AdministradorForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Pesquisador
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pesquisador.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.cargo = 'Administrador'
        if commit:
            user.save()
            grupo_administrador = Group.objects.get(name='Administrador')
            user.groups.add(grupo_administrador)
        return user