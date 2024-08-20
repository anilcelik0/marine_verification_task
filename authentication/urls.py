from django.urls import path
from .views import AuthSigninView, AuthSignupView, logout_view, BaseView


urlpatterns = [
    path('', BaseView, name='base'),
    path('login', AuthSigninView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup', AuthSignupView, name='signup'),
]