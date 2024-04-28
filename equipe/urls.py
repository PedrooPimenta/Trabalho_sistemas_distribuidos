from django.urls import path
from .views import ListarEquipe, CriarEquipe, EditarEquipe, ExcluirEquipe

urlpatterns = [
    path('', ListarEquipe.as_view(), name='listar_equipe'),
    path('criar/', CriarEquipe.as_view(), name='criar_equipe'),
    path('editar/<int:pk>/', EditarEquipe.as_view(), name='editar_equipe'),
    path('excluir/<int:pk>/', ExcluirEquipe.as_view(), name='excluir_equipe'),
]
