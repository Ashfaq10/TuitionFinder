from django.urls import path
from tuition.views import HomeStudentView, HomeTutorView, TuitionDetailView, TuitorDetailView, TuitionAdd, TuitionDelete

app_name = 'tuition'

urlpatterns = [

    path("student/", HomeStudentView.as_view(), name = 'homepage_student'),
    path("tutor/", HomeTutorView.as_view(), name = 'homepage_tutor'),
    path("tuition-details/<int:id>/", TuitionDetailView.as_view(), name = 'tuition_detail'),
    path("tuitor-details/<int:id>/", TuitorDetailView.as_view(), name = 'tuitor_detail'),
    path("tuition-add/", TuitionAdd.as_view(), name = 'tuition_add'),
    path("tuition-delete/<int:id>/", TuitionDelete.as_view(), name = 'tuition_delete'),
    
  
]
