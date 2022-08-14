from django.urls import path
from tuition.views import HomeView

app_name = 'tuition'

urlpatterns = [
    path("", HomeView.as_view(), name = 'homepage')
    
]
