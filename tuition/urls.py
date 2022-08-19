from django.urls import path
from tuition.views import HomeStudentView, HomeTutorView, TuitionUpdate,  TuitionAdd, TuitionDelete, homepage


app_name = 'tuition'

urlpatterns = [
    path("", homepage, name = 'homepage'),
    path("student/", HomeStudentView.as_view(), name = 'homepage_student'),
    path("tutor/", HomeTutorView.as_view(), name = 'homepage_tutor'),
    path("tuition-add/", TuitionAdd.as_view(), name = 'tuition_add'),
    path("tuition-delete/<int:id>/", TuitionDelete.as_view(), name = 'tuition_delete'),
    path("tuition-update/<int:id>/", TuitionUpdate.as_view(), name = 'tuition_update'),
    
]
