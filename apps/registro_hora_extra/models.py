from django.db import models

# Create your models here.
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horaextra = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('edit_funcionarios', args=(self.funcionario.id, ))
