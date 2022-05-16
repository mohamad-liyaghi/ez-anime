from django.shortcuts import redirect

class NotAuthenticatedMixin():
    def dispatch(self,request, *args, **kwargs):
        if self.request.user.is_authenticated:
           return redirect ("movie:home")
        else:
            return super().dispatch(request, *args, **kwargs)