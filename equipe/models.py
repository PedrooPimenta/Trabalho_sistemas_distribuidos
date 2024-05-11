from django.db import models
from datetime import datetime


class Titulacao(models.TextChoices):
    GRADUANDO = "Graduando"
    GRADUACAO = "Graduação"
    MESTRADO = "Mestrado"
    DOUTORADO = "Doutorado"


class Cargo(models.TextChoices):
    ALUNO = "Aluno"
    PROFESSOR = "Professor"
    TECNICO = "Técnico"


class Pesquisador(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Pesquisador")
    nivel = models.CharField(
        max_length=10, choices=Titulacao.choices, verbose_name="Titulação")
    lattes = models.URLField(blank=True, null=True, verbose_name="Lattes")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Linkedin")
    researchgate = models.URLField(
        blank=True, null=True, verbose_name="Research Gate")
    email = models.EmailField(verbose_name="E-mail")
    data_criacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação")
    ativo = models.BooleanField(default=False)
    cargo = models.CharField(
        max_length=10, choices=Cargo.choices, verbose_name="Cargo")

    def __str__(self):
        return f"{self.nome} ({self.nivel})"
