from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic

from tuition.utils.users_forms import UserUpdateForm
from tuition.models.users_models import User



class ProfileView(generic.View):
    template_name = "users/profile_template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user': request.user})

class LoginView(generic.View):
    template_name = 'users/login_template.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            
            return redirect('tuition:homepage')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, self.template_name, {'error': 'Username/password Invalid'})
        login(request, user)
        return redirect('tuition:homepage')

@login_required(login_url='tuition:login')
def logoutView(request):
    logout(request)
    return redirect('tuition:login')

class RegistrationView(generic.View):
    template_name = 'users/registration_template.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('tuition:homepage')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_type = request.POST.get('user_type')


        try:
            user = User.objects.create_user(username=username, password=password,
                                            email=email, first_name=first_name, last_name=last_name, 
                                            location= location,phone=phone, user_type=user_type)
            user.set_password(password)
            user.save()

        except Exception as e:
            print(e)
            return render(request, self.template_name, {'error': 'Username already exists!'})

        if user:
            login(request, user)
            
            return redirect('tuition:homepage')
        return render(request, self.template_name, {'error': 'Unknown Error!'})

class UpdateProfileView(generic.View):
    template_name = "users/update_profile_template.html"

    form_class = UserUpdateForm
    login_url = reverse_lazy('user:login')


    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form =  self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('tuition:profile', username=request.user.username)
        print(form.errors)
        return render(request, self.template_name, {'form': form})
