from django.shortcuts import render
from django.views import generic


# Create your views here.

class HomeView(generic.View):
    template_name = "tuition/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class TuitionDetailView(generic.View):
    template_name = "tuition/tuition_detail.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class TuitorDetailView(generic.View):
    template_name = "tuition/tuitor_detail.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class TuitionAdd(generic.View):
    template_name = "tuition/tuition_add.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TuitionDelete(generic.View):
    template_name = "tuition/tuition_delete.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

