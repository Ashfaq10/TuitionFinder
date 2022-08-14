from django.shortcuts import render
from django.views import generic

# Create your views here.

class ProfileView(generic.View):
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

