from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra


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
