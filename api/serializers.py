from rest_framework import serializers
from equipe.models import Pesquisador
from monografias.models import Monografia


class MonografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monografia
        fields = ['id', 'titulo', 'autor', 'orientador',
                  'coorientador', 'banca_examinadora', 'resumo', 'palavras_chave', 'data_entrega', 'nota_final', 'area_concentracao', 'arquivos']
class PesquisadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesquisador
        fields = ['id', 'username', 'email', 'nivel', 'lattes', 'linkedin', 'researchgate', 'cargo']