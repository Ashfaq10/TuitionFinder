from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from tuition.utils.tuition_forms import TuitionModelForm
from tuition.models.users_models import User
from tuition.models.tuiton_models import Tuition
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeStudentView(generic.View):
    template_name = "tuition/home_student.html"

    def get(self, request, *args, **kwargs):
        tutors= User.objects.filter(user_type='tutor')
        return render(request, self.template_name,{"tutors":tutors})

class HomeTutorView(generic.View):
    template_name = "tuition/home_tutor.html"
    

    def get(self, request, *args, **kwargs):
        qs = request.GET.get('qs')
        tuitions =Tuition.objects.all()
        if qs:
            tuitions = tuitions.filter(location__icontains=qs)
        return render(request, self.template_name,{"tuitions":tuitions})

class TuitionAdd(generic.CreateView):
    template_name = "tuition/tuition_add.html"
    success_url = reverse_lazy("tuition:homepage")
    login_url = reverse_lazy('tutiton:login')
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




class TuitionDelete(LoginRequiredMixin,generic.View):
    login_url = reverse_lazy('tuition:login')

    def get(self, request, *args, **kwargs):
        tuition = Tuition.objects.get(id=kwargs.get("id"))
        username = tuition.provider.username
        tuition.delete()
        return redirect('tuition:profile', username=username)

class TuitionUpdate(generic.View):
    template_name = "tuition/tuition_update.html"
    login_url = reverse_lazy('tuition:login')
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
            return redirect('tuition:profile', username=self.request.user)
        # print(form.errors)
        return render(request, self.template_name, {'form': form})


@login_required
def homepage(request):
    if request.user.user_type == 'tutor':
        return redirect('tuition:homepage_tutor')
    return redirect('tuition:homepage_student')
    