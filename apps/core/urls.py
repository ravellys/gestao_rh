from django.contrib import admin
from django.urls import path

from apps.core.views import home, GroupViewSet, UserViewSet
from apps.core.dash_app import exemplo



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', home, name='home'),
]
