from django.db import models

# Create your models here.
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('edit_funcionarios', args=(self.pertence.id, ))
