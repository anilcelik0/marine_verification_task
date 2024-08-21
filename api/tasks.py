from celery import shared_task
from .models import OtpAuth
import random

# Toools

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

# Tasks

@shared_task
def update_otp_token(**kwargs):
    print(kwargs["id"])
    user = OtpAuth.objects.get(id=int(kwargs["id"]))
    user.token = create_otp()
    print(user.user.username)
    print(user.token)
    user.save()
    print(user.token)