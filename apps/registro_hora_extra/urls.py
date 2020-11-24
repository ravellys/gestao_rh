from django.contrib import admin
from django.urls import path
from apps.registro_hora_extra.views import RegistroHoraExtraListView, RegistroHoraExtraUpdateView, \
    RegistroHoraExtraDeleteView, RegistroHoraExtraCreateView

urlpatterns = [
    path('list_hora_extra/', RegistroHoraExtraListView.as_view(), name='list_hora_extra'),
    path('novo/', RegistroHoraExtraCreateView.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', RegistroHoraExtraUpdateView.as_view(), name='edit_hora_extra'),
    path('deletar/<int:pk>', RegistroHoraExtraDeleteView.as_view(), name='delete_hora_extra'),
]
