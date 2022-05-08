from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from cast.forms import CastForm
# Create your views here.


class AddGenre(LoginRequiredMixin,FormView):
    template_name = "cast/add-genre.html"
    form_class = CastForm
    def form_valid(self, form):
        form.save()
        return redirect ("cast:add-genre")
    def form_invalid(self, form):
        return redirect ("cast:add-genre")        
