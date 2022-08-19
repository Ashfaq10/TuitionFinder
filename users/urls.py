from django.urls import path
from users.views import LoginView, ProfileView, RegistrationView, UpdateProfileView, logoutView 

app_name = 'users'

urlpatterns = [
    path("profile/<str:username>/", ProfileView.as_view(), name = 'profile'),
    path("login/", LoginView.as_view(), name = 'login'),
    path("registration/", RegistrationView.as_view(), name = 'registration'),
    path("logout/", logoutView, name = 'logout'),
    path("update_profile/<str:username>/", UpdateProfileView.as_view(), name = 'update_profile'),
]
