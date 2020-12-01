from django.contrib import admin
from django.urls import path
from apps.registro_hora_extra.views import RegistroHoraExtraListView, RegistroHoraExtraUpdateView, \
    RegistroHoraExtraDeleteView, RegistroHoraExtraCreateView, RegistroHoraExtraBaseUpdateView, UtilizouHoraExtraView, \
    NaoUtilizouHoraExtraView

urlpatterns = [
    path('list_hora_extra/', RegistroHoraExtraListView.as_view(), name='list_hora_extra'),
    path('novo/', RegistroHoraExtraCreateView.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>', RegistroHoraExtraUpdateView.as_view(), name='edit_hora_extra'),
    path('editar/<int:pk>', RegistroHoraExtraBaseUpdateView.as_view(), name='edit_hora_extra_base'),
    path('deletar/<int:pk>', RegistroHoraExtraDeleteView.as_view(), name='delete_hora_extra'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtraView.as_view(), name='utilizou-hora-extra'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtraView.as_view(), name='nao-utilizou-hora-extra'),
]
