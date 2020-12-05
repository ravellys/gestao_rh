from django.contrib import admin
from django.urls import path

from apps.core.views import home
from apps.core.dash_app import exemplo

urlpatterns = [
    path('', home, name='home'),
]
