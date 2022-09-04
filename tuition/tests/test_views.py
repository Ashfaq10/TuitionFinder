from django.test import TestCase, Client
from django.urls import reverse
from tuition.models.tuiton_models import Tuition
from tuition.models.users_models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test')
        self.user.set_password('test')
        self.user.save()
        self.client.force_login(self.user)
        self.recipe = Tuition.objects.create(provider=self.user, location ="Dhanmondi",salary="4000", level="class10", subject="Physics")

    def test_home_student_view(self):
        url = reverse("tuition:homepage_student")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "tuition/home_student_template.html")
        
    def test_home_tutor_view(self):
        url = reverse("tuition:homepage_tutor")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "tuition/home_tutor_template.html")

    def test_tuition_add_view(self):
        url = reverse("tuition:tuition_add")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "tuition/tuition_add_template.html")

    def test_profile_view(self):
        url = reverse("tuition:profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile_template.html")
    
    def test_update_profile_view(self):
        url = reverse("tuition:update_profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/update_profile_template.html")
    
    
