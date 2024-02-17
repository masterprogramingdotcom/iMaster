
from django.urls import path
from control.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]
