from rest_framework import serializers
from .models import OtpAuth
from django.contrib.auth.models import User


class OtpAuthSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = OtpAuth
        fields = ('id','user', 'token')


class LoginWithOtpSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=200)
    token = serializers.CharField(max_length=20)
    