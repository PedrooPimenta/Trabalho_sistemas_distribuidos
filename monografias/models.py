from django.db import models

class Monografia(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    orientador = models.CharField(max_length=100)
    coorientador = models.CharField(max_length=100, blank=True, null=True)
    resumo = models.TextField()
    palavras_chave = models.CharField(max_length=100)
    data_entrega = models.DateField()
    banca_examinadora = models.CharField(max_length=100, blank=True, null=True)
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    area_concentracao = models.CharField(max_length=100, blank=True, null=True)
    arquivo = models.FileField(upload_to='monografias/%Y/%m/%d')

    def __str__(self):
        return self.titulo
