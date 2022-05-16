from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from cast.forms import GenreForm,CastForm
# Create your views here.


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
        form.save()
        return redirect ("movie:home")
    def form_invalid(self, form):
        return redirect ("cast:add-cast")  
    
