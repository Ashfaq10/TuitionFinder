from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from .models import User



# Create your views here.

class ProfileView(generic.View):
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class LoginView(generic.View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'student':
                return redirect('tuition:homepage_student')
            else:
                return redirect('tuition:homepage_tutor')


            

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, self.template_name, {'error': 'Username/password Invalid'})
        login(request, user)

        if request.user.user_type == 'student':
            return redirect('tuition:homepage_student')
        else:
            return redirect('tuition:homepage_tutor')

@login_required(login_url='users:login')
def logoutView(request):
    logout(request)
    return redirect('users:login')

class RegistrationView(generic.View):
    template_name = 'users/registration.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == "student":
                return redirect('tuition:homepage_student')
            return redirect('tuition:homepage_tutor')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type')


        try:
            user = User.objects.create_user(username=username, password=password,
                                            email=email, first_name=first_name, last_name=last_name, user_type=user_type)
            user.set_password(password)
            user.save()

        except Exception as e:
            print(e)
            return render(request, self.template_name, {'error': 'Username already exists!'})

        if user:
            login(request, user)
            if user.user_type == "student":
                return redirect('tuition:homepage_student')
            return redirect('tuition:homepage_tutor')
        return render(request, self.template_name, {'error': 'Unknown Error!'})

class UpdateProfileView(generic.View):
    template_name = "users/update_profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
