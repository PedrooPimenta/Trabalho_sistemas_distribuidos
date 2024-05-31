from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from equipe import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from home import views as home_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('monografias/', include('monografias.urls')),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', home_views.index, name='home'),
    path("equipe/", include('equipe.urls'), name='equipe'),
    path('api/v1/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
