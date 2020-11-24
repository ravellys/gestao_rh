from django.contrib import admin
from django.urls import path

from apps.documentos.views import DocumentoCreateView

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreateView.as_view(), name='create_documento'),
    #path('editar/<int:pk>', EmpresaUpdateView.as_view(), name='edit_empresa'),
]
