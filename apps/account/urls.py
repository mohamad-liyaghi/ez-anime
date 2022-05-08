from django.urls import path
from .views import (
    Login, Logout, Register)

app_name = "account"

urlpatterns = [
    path("login/",Login.as_view(),name="login"),
    path("logout/",Logout,name="logout"),
    path("register/",Register.as_view(),name="register")
]