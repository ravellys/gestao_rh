from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from apps.empresas.models import Empresa


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return redirect(Empresa.get_absolute_url(Empresa))

class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['nome']
