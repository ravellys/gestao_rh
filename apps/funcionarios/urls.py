from django.contrib import admin
from django.urls import path

from apps.funcionarios.views import FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView, \
    FuncionarioCreateView, relatorio_funcionarios, PDF, PDFTemplateView

urlpatterns = [
    path('list_funcionarios/', FuncionarioListView.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioCreateView.as_view(), name='create_funcionarios'),
    path('editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='edit_funcionarios'),
    path('deletar/<int:pk>/', FuncionarioDeleteView.as_view(), name='delete_funcionarios'),
    path('pdf-reportlab/', relatorio_funcionarios, name='pdf-reportlab'),
    path('pdf-xhtml2pdf/', PDF.as_view(), name='pdf-xtml2pdf'),
    path('pdf-xhtml2pdf-debug/', PDFTemplateView.as_view(), name='pdf-xtml2pdf-debug'),
]
