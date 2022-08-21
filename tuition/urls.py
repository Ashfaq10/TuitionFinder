from django.urls import path
from tuition.views.tuition_views import HomeStudentView, HomeTutorView, TuitionUpdate,  TuitionAdd, TuitionDelete, homepage
from tuition.views.users_views import LoginView, ProfileView, RegistrationView, UpdateProfileView, logoutView 


app_name = 'tuition'

urlpatterns = [
    path("", homepage, name = 'homepage'),
    path("student/", HomeStudentView.as_view(), name = 'homepage_student'),
    path("tutor/", HomeTutorView.as_view(), name = 'homepage_tutor'),
    path("tuition-add/", TuitionAdd.as_view(), name = 'tuition_add'),
    path("tuition-delete/<int:id>/", TuitionDelete.as_view(), name = 'tuition_delete'),
    path("tuition-update/<int:id>/", TuitionUpdate.as_view(), name = 'tuition_update'),
    path("profile/<str:username>/", ProfileView.as_view(), name = 'profile'),
    path("login/", LoginView.as_view(), name = 'login'),
    path("registration/", RegistrationView.as_view(), name = 'registration'),
    path("logout/", logoutView, name = 'logout'),
    path("update_profile/<str:username>/", UpdateProfileView.as_view(), name = 'update_profile'),
]
