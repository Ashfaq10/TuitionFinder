from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from tuition.forms import TuitionModelForm
from users.models import User
from tuition.models import Tuition
from django.contrib.auth.decorators import login_required


# Create your views here.

class HomeStudentView(generic.View):
    template_name = "tuition/home_student.html"

    def get(self, request, *args, **kwargs):
        tutors= User.objects.all()
        return render(request, self.template_name,{"tutors":tutors})

class HomeTutorView(generic.View):
    template_name = "tuition/home_tutor.html"
    

    def get(self, request, *args, **kwargs):
        tuitions =Tuition.objects.all()
        return render(request, self.template_name,{"tuitions":tuitions})

class TuitionAdd(generic.CreateView):
    template_name = "tuition/tuition_add.html"
    success_url = reverse_lazy("tuition:homepage")
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'tuition:homepage'
    form_class = TuitionModelForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.provider = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)




class TuitionDelete(generic.View):
    template_name = "tuition/tuition_delete.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
class TuitionUpdate(generic.View):
    template_name = "tuition/tuition_update.html"
    login_url = reverse_lazy('users:login')
    form_class = TuitionModelForm

    def get_object(self):
        return Tuition.objects.get(id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_object())
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=self.request.user)
        # print(form.errors)
        return render(request, self.template_name, {'form': form})


@login_required
def homepage(request):
    if request.user.user_type == 'tutor':
        return redirect('tuition:homepage_tutor')
    return redirect('tuition:homepage_student')
    