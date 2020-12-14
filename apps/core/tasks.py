# Create your tasks here

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_relatorio():
    send_mail(
        subject='Subject here',
        message='Here is the mensage',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['lucas.ravellys@ufpe.br', 'abraao.vilanova@ufpe.br'],
        fail_silently=False,
    )
    return True

