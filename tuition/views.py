from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomeView(generic.View):
    template_name = "tuition/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

