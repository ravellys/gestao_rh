from django.contrib import admin
from django.urls import path

from apps.departamentos.views import DepartamentoListView, DepartamentoCreateView, DepartamentoUpdateView, \
    DepartamentoDeleteView

urlpatterns = [
    path('list_departamentos/', DepartamentoListView.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreateView.as_view(), name='create_departamentos'),
    path('edit/<int:pk>', DepartamentoUpdateView.as_view(), name='edit_departamentos'),
    path('delete/<int:pk>', DepartamentoDeleteView.as_view(), name='delete_departamentos'),
]
