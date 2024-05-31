from django.db import models

from equipe.models import Pesquisador


class Monografia(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.OneToOneField(
        Pesquisador, on_delete=models.SET_NULL, null=True, related_name='monografia_escrita')
    orientador = models.ForeignKey(
        Pesquisador, on_delete=models.SET_NULL, null=True, related_name='monografias_orientadas')
    coorientador = models.ForeignKey(
        Pesquisador, on_delete=models.SET_NULL, max_length=100, blank=True, null=True)
    resumo = models.TextField()
    palavras_chave = models.CharField(max_length=100)
    data_entrega = models.DateTimeField(auto_now_add=True)
    banca_examinadora = models.ManyToManyField(
        Pesquisador, related_name='monografias_banca', verbose_name="Banca Examinadora")
    nota_final = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    area_concentracao = models.CharField(max_length=100, blank=True, null=True)
    arquivos = models.FileField(upload_to='arquivos/')

    def __str__(self):
        return self.titulo
