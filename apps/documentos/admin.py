from django.contrib import admin

# Register your models here.
from apps.documentos.models import Documento

admin.site.register(Documento)
