from django.urls import path
from .views import ListarEquipe, CriarEquipe, EditarEquipe, ExcluirEquipe,RegistrarUsuario, RegistrarProfessor , RegistrarAdministrador, ListarMonografiasProfessor
from . import views
urlpatterns = [
    path('', ListarEquipe.as_view(), name='listar_equipe'),
    path('criar/', CriarEquipe.as_view(), name='criar_equipe'),
    path('editar/<int:pk>/', EditarEquipe.as_view(), name='editar_equipe'),
    path('excluir/<int:pk>/', ExcluirEquipe.as_view(), name='excluir_equipe'),
    path('criar_usuario', RegistrarUsuario.as_view(), name='novo_usuario'),
    path('cadastrar_prof',RegistrarProfessor.as_view(), name='cadastrar_professor'),
    path('cadastrar_adm',RegistrarAdministrador.as_view(), name='cadastrar_administrador'),
    path('monografias_prof', ListarMonografiasProfessor.as_view(), name='monografias_professor'),
]
