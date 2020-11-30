from django.contrib import admin
from django.urls import path

from apps.documentos.views import DocumentoCreateView, DocumentoUpdateView

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreateView.as_view(), name='create_documento'),
    path('editar/<int:pk>', DocumentoUpdateView.as_view(), name='edit_documento'),
]
