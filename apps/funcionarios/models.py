from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Sum
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

    @property
    def total_hora_extra(self):
         return self.registrohoraextra_set.aggregate(soma_horaextra=Sum('horaextra'))['soma_horaextra']

    def get_absolute_url(self):
        return reverse('list_funcionarios')
