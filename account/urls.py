
from django.urls import path
from account.views import LoginAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login")
]
