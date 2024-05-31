from rest_framework.routers import DefaultRouter
from api.views import MonografiaViewSet, PesquisadorViewSet

app_name = 'api'

# trailing_slash especifica que não é necessário o uso de barras / no final da URL
router = DefaultRouter(trailing_slash=False)
router.register(r'monografias', MonografiaViewSet)
router.register(r'pesquisador', PesquisadorViewSet)
urlpatterns = router.urls
