import csv
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra

import pandas as pd


class RegistroHoraExtraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class RegistroHoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegistroHoraExtraBaseUpdateView(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('edit_hora_extra_base', args=(self.object.id, ))

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraBaseUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RegistroHoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class RegistroHoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtraView(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario
        horas = funcionario.total_hora_extra

        response = json.dumps(
            {'mensagem': 'Requisição Executada',
             'horas': float(horas)}
        )
        return HttpResponse(response, content_type='application/json')


class NaoUtilizouHoraExtraView(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario
        horas = funcionario.total_hora_extra

        response = json.dumps(
            {'mensagem': 'Requisição Executada',
             'horas': float(horas)}
        )
        return HttpResponse(response, content_type='application/json')


class ExportarCsvView(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio_he.csv"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Funcionário', 'Motivo', 'Horas Extra'])

        for registro in registro_he:
            writer.writerow([registro.funcionario, registro.motivo, registro.horaextra])

        return response


class ExportarExcelView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/xlsx')
        response['Content-Disposition'] = 'attachment; filename="relatorio_he.xlsx"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)
        lista = [[registro.funcionario, registro.motivo, registro.horaextra] for registro in registro_he]
        df = pd.DataFrame(lista, columns=['Funcionário', 'Motivo', 'Horas Extra'])
        df.to_excel(response, sheet_name="sheet_1")

        return response
