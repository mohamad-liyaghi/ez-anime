from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid

from element.models import Cast
from element.forms import CastForm

class CastProfile(DetailView):
    '''Cast Profile page'''
    template_name = "element/cast/cast-profile.html"

    def get_object(self, **kwarg):
        return get_object_or_404(Cast, token=self.kwargs['token'])


class AddCast(LoginRequiredMixin, FormView):
    '''Add actor or Director to database'''

    template_name = "element/cast/add-cast.html"
    form_class = CastForm

    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:10]
        form.save()
        return redirect("movie:home")

    def form_invalid(self, form):
        return redirect("element:add-cast")


class UpdateCast(LoginRequiredMixin, UpdateView):
    '''Update a cast information'''

    template_name = "element/cast/update-cast.html"
    fields = ["full_name", 'biography', 'birthday', 'role', 'avatar']
    success_url = "/"

    def get_object(self):
        return get_object_or_404(Cast, token=self.kwargs['token'])

