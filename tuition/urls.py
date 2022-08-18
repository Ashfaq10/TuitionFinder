from django.urls import path
from tuition.views import HomeView, TuitionDetailView, TuitorDetailView, TuitionAdd, TuitionDelete

app_name = 'tuition'

urlpatterns = [

    path("", HomeView.as_view(), name = 'homepage'),
    path("tuition-details/<int:id>/", TuitionDetailView.as_view(), name = 'tuition_detail'),
    path("tuitor-details/<int:id>/", TuitorDetailView.as_view(), name = 'tuitor_detail'),
    path("tuition-add/", TuitionAdd.as_view(), name = 'tuition_add'),
    path("tuition-delete/<int:id>/", TuitionDelete.as_view(), name = 'tuition_delete'),
    
  
]
