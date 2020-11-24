from django.contrib import admin
from django.urls import path
from apps.registro_hora_extra.views import RegistroHoraExtraListView

urlpatterns = [
    path('list_hora_extra/', RegistroHoraExtraListView.as_view(), name='list_hora_extra'),
]
