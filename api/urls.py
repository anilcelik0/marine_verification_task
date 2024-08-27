from django.urls import path, include
from .views import OtpAuthViewset, LoginWithOtpViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tokens', OtpAuthViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginWithOtpViewset.as_view(), name="login_api")
]