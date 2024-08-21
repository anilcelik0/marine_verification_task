from django.shortcuts import render
from .serializers import OtpAuthSerializer, LoginWithOtpSerializer
from .models import OtpAuth
from django.contrib.auth.models import User
from rest_framework.viewsets import mixins
from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import login
from rest_framework.response import Response

# Create your views here.

class OtpAuthViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = OtpAuth.objects.all()
    serializer_class = OtpAuthSerializer



class LoginWithOtpViewset(ListCreateAPIView):
    
    queryset = OtpAuth.objects.all()
    serializer_class = LoginWithOtpSerializer
    
    def create(self, request, *args, **kwargs):
        username = request.data["user"]
        token = request.data["token"]
        user = User.objects.filter(username=username)
        
        if user.exists():
            user = user.first()
            
            if user.otp_token.token == token:
                login(request, user)
                return Response({'Success':'Login Success'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'Failure':'OTP is wrong or it can be change'}, status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response({'Failure':'User not exists'}, status=status.HTTP_400_BAD_REQUEST)