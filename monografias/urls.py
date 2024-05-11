from django.urls import path
from .views import ListarMonografias, CriarMonografia, EditarMonografia, ExcluirMonografia

urlpatterns = [
    path('', ListarMonografias.as_view(), name='listar_monografias'),
    path('criar/', CriarMonografia.as_view(), name='criar_monografia'),
    path('editar/<int:pk>/', EditarMonografia.as_view(), name='editar_monografia'),
    path('excluir/<int:pk>/', ExcluirMonografia.as_view(),
         name='excluir_monografia'),
]
