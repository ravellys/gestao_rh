from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamentos.models import Departamento


class DepartamentoListView(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

class DepartamentoCreateView(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        return super(DepartamentoCreateView, self).form_valid(form)

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    fields = ['nome']

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
