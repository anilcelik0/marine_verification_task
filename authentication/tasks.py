from celery import shared_task
from .models import SıgnUpToken
from django.utils import timezone


@shared_task
def clean_token():
    SıgnUpToken.objects.filter(expiration_date__lt=timezone.now()).delete()