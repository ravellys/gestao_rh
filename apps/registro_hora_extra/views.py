from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class RegistroHoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    fields = '__all__'

class RegistroHoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class RegistroHoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    fields = '__all__'
