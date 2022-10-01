from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid

from element.models import Cast
from element.forms import CastForm


# Create your views here.

class CastProfile(DetailView):
    template_name = "element/element-profile.html"

    def get_object(self, **kwarg):
        return get_object_or_404(Cast, token=self.kwargs['token'])

class AddCast(LoginRequiredMixin, FormView):
    template_name = "element/add-element.html"
    form_class = CastForm

    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:10]
        form.save()
        return redirect("movie:home")

    def form_invalid(self, form):
        return redirect("element:add-element")


class UpdateCast(LoginRequiredMixin, UpdateView):
    template_name = "element/update-element.html"
    fields = "__all__"
    success_url = "/"

    def get_object(self):
        return get_object_or_404(Cast, token=self.kwargs['token'])
