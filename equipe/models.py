from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from auditlog.registry import auditlog


class Titulacao(models.TextChoices):
    GRADUACAO = "Graduação"
    MESTRADO = "Mestrado"
    DOUTORADO = "Doutorado"


class Cargo(models.TextChoices):
    ALUNO = "Aluno"
    PROFESSOR = "Professor"
    ADMNISTRADOR = "Administrador"


class Pesquisador(AbstractUser):
    nivel = models.CharField(
        max_length=10, choices=Titulacao.choices, verbose_name="Titulação")
    lattes = models.URLField(blank=True, null=True, verbose_name="Lattes")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Linkedin")
    researchgate = models.URLField(
        blank=True, null=True, verbose_name="Research Gate")
    data_criacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação")
    ativo = models.BooleanField(default=False)
    cargo = models.CharField(
        max_length=15, choices=Cargo.choices, verbose_name="Cargo")

    def __str__(self):
        return f"{self.username} ({self.nivel})"
auditlog.register(Pesquisador)
