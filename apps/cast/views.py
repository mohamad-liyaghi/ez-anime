from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid

from cast.models import Cast
from cast.forms import GenreForm,CastForm
# Create your views here.

class CastProfile(DetailView):
    template_name = "cast/cast-profile.html"
    def get_object(self, **kwarg):
        return get_object_or_404(Cast,token= self.kwargs['token'])

class AddGenre(LoginRequiredMixin,FormView):
    template_name = "cast/add-genre.html"
    form_class = GenreForm
    def form_valid(self, form):
        form.save()
        return redirect ("movie:home")
    def form_invalid(self, form):
        return redirect ("cast:add-genre")        


class AddCast(FormView):
    template_name = "cast/add-cast.html"
    form_class = CastForm
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:10]
        form.save()

        return redirect ("movie:home")
    def form_invalid(self, form):
        return redirect ("cast:add-cast")  
    
