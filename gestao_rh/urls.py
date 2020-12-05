"""gestao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from apps.core.views import home, GroupViewSet, UserViewSet


from django.urls import include, path
from rest_framework import routers

from apps.funcionarios.api.viewsets import FuncionarioViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'api/funcionario', FuncionarioViewSet)
router.register(r'api/hora-extra', FuncionarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departamentos/', include('apps.departamentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
