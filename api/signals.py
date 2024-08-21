from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import OtpAuth
from django_celery_beat.models import IntervalSchedule as Period, PeriodicTask
import json
import random

# Tools

def create_otp():
    while True:
        char = '0123456789abcdefghijklmnopqrstuvwxyz?@!#%+-*'
        id = ""
        for i in range(20):
            id += random.choice(char)
        if OtpAuth.objects.filter(token=id).exists():
            continue
        else:
            return id


#Signals

@receiver(post_save, sender=User)
def create_otp_token(sender, instance, created, **kwargs):
    if created:
        token = OtpAuth.objects.create(user=instance, token=create_otp())
        period = Period.objects.get(id=3)
        PeriodicTask.objects.create(name="otp-"+str(instance.id),
                            interval=period,
                            description="otp refresh",
                            task="api.tasks.update_otp_token",
                            kwargs=json.dumps({"id":token.id})
                            )
