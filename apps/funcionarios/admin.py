from django.contrib import admin

# Register your models here.
from apps.funcionarios.models import Funcionario

admin.site.register(Funcionario)