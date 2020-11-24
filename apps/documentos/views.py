from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from apps.documentos.models import Documento


class DocumentoCreateView(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form)
        form.instance.pertence_id = self.kwargs['funcionario_id']
        print(form)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



