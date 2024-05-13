from rest_framework import serializers
from monografias.models import Monografia


class MonografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monografia
        fields = ['id', 'titulo', 'autor', 'orientador',
                  'coorientador', 'banca_examinadora', 'resumo', 'palavras_chave', 'data_entrega', 'nota_final', 'area_concentracao', 'arquivos']
