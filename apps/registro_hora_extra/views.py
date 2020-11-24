from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)