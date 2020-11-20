from django.contrib import admin
from django.urls import path

from apps.funcionarios.views import home

urlpatterns = [
    path('', home),
]
