from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from xhtml2pdf import pisa

from apps.funcionarios.models import Funcionario

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


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


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(200, 810, "Hello world.")

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)
    y = 750

    for funcionario in funcionarios:
        str_ = f'NOME: {funcionario.nome} | HORAS: {funcionario.total_hora_extra}'
        p.drawString(50, y, str_)
        y -= 20

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(html.encode("UTF-8"), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type="application/pdf"
            )
            response['Content-Disposition'] = f'attachment; filename={filename}.pdf'
            return response
        else:
            return HttpResponse("ERROR", status=400)


class PDF(View):

    def get(self, request):
        params = {
            'hoje': 'variavel hoje',
            'vendas': 'variavel vendas',
            'request': request
        }
        return Render.render(path='funcionarios/relatorio.html', params=params, filename='relatorio_pdf.pdf')


class PDFTemplateView(TemplateView):
    template_name = 'funcionarios/relatorio.html'
