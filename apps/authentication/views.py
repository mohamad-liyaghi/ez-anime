
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import RegisterForm
from .mixins import NotAuthenticatedMixin
# Create your views here.
class Login(NotAuthenticatedMixin,LoginView):
    template_name = "authentication/login-user.html"
    def get_success_url(self):
        return reverse_lazy('movie:home')


def Logout(request):
    if request.user.is_authenticated:
	    logout(request)
	    return redirect('authentication:login')
    else:
        return redirect('movie:home')

class Register(NotAuthenticatedMixin,CreateView):
    form_class = RegisterForm
    template_name = 'authentication/register-user.html'
    def form_valid(self, form):
        form.save()
        return  redirect('movie:home')
    def form_invalid(self, form):
        print(form.errors)
        return redirect("authentication:register")