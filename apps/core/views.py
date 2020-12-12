from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# API imports
from apps.core.api.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .tasks import send_relatorio

@login_required()
def home(requests):
    data = {'usuario': requests.user}
    return render(requests, 'core/index.html', context=data)


def celery(requests):
    send_relatorio.delay()
    return HttpResponse('email enviado')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]