from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tuition.views.tuition_views import(HomeStudentView, HomeTutorView, TuitionAdd,TuitionDelete,TuitionUpdate)
from tuition.views.users_views import(ProfileView, LoginView, logoutView,RegistrationView, UpdateProfileView)

class TestUrls(SimpleTestCase):
    def test_home_student_url_is_resolved(self):
        url = reverse("tuition:homepage_student")
        self.assertEquals(resolve(url).func.view_class,HomeStudentView)
    def test_home_tutor_url_is_resolved(self):
        url = reverse("tuition:homepage_tutor")
        self.assertEquals(resolve(url).func.view_class,HomeTutorView)
    def test_tuition_add_url_is_resolved(self):
        url = reverse("tuition:tuition_add")
        self.assertEquals(resolve(url).func.view_class, TuitionAdd)
    def test_tuition_delete_url_is_resolved(self):
        url = reverse("tuition:tuition_delete", args=[10])
        self.assertEquals(resolve(url).func.view_class, TuitionDelete)
    def test_tuition_update_url_is_resolved(self):
        url = reverse("tuition:tuition_update", args=[10])
        self.assertEquals(resolve(url).func.view_class, TuitionUpdate)
    def test_user_profile_url_is_resolved(self):
        url = reverse('tuition:profile', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ProfileView)

    def test_login_url_is_resolved(self):
        url = reverse('tuition:login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_registration_url_is_resolved(self):
        url = reverse('tuition:registration')
        self.assertEquals(resolve(url).func.view_class, RegistrationView)

    def test_user_profile_update_url_is_resolved(self):
        url = reverse('tuition:update_profile', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, UpdateProfileView)

    def test_logout_url_is_resolved(self):
        url = reverse('tuition:logout')
        self.assertEquals(resolve(url).func, logoutView)
    