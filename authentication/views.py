from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import SıgnUpToken
import random
from django.utils import timezone
import datetime

# Tools
def create_token():
    while True:
        char = '0123456789abcdefghijklmnopqrstuvwxyz'
        id = ""
        for i in range(10):
            id += random.choice(char)
        if SıgnUpToken.objects.filter(token=id).exists():
            continue
        else:
            return id

def expiration_date():
    now = datetime.datetime.now()
    date = now + datetime.timedelta(minutes=1)
    return date

# Create your views here.


def BaseView(request):
    return render(request, 'pages/base.html')


def AuthSignupView(request):
    
    if request.method =="POST":
        token_str = request.POST["token"]
        token = SıgnUpToken.objects.filter(token=token_str).first()
        
        if token.expiration_date > timezone.now():
            form = SignUpForm(request.POST)
            if form.is_valid():
                
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Kayıt başarı ile tamamlandı Giriş yapbilirsiniz')

                return redirect('login')
            else:
                messages.add_message(request, messages.WARNING, 'Bilgiler hatlı tekrar deneyin')
                return redirect('signup')
        
        else:
            messages.add_message(request, messages.WARNING, 'Token süresi doldu tekrar deneyin')
            return redirect('signup')
    
    form = SignUpForm
    token = SıgnUpToken.objects.create(token=create_token(), expiration_date=expiration_date())
    context = {
        'form':form,
        'token':token.token
    }
    return render(request, 'pages/sign-up.html', context)


class AuthSigninView(FormView):
    template_name = 'pages/sign-in.html'
    form_class = LoginForm
    success_url = reverse_lazy('base')

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return super().post(request, *args, **kwargs)
        
        else:
            # return HttpResponseRedirect(reverse_lazy('auth:signin'))
            messages.add_message(request, messages.ERROR, "Login Failed")
            return HttpResponseRedirect(reverse_lazy('login'))

        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))
