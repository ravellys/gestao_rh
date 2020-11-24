from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.funcionarios.models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario

    # listar apenas funcionários da empresa
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    # retorna o url passado para reverse_lazy
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        # criar funcionario e não comitar para o banco
        funcionario = form.save(commit=False)
        # criar empresa para funcionário
        funcionario.empresa = self.request.user.funcionario.empresa
        # criar usuário para funcionário
        username = " ".join(funcionario.nome.split(' ')[:2])
        funcionario.user = User.objects.create(username=username)
        # salvar funcionário
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)