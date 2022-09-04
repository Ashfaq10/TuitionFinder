from django.test import TestCase
from tuition.models.tuiton_models import Tuition
from tuition.models.users_models import User

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser'
        )
        self.tuition = Tuition.objects.create(
            provider = self.user,
            location = "Dhanmondi",
            phone = "01879904641",
            salary = "5000",
            requirements = "Anyone",
            level = "class 5",
            subject = "Bangla"

        )  
    def test_user_model(self):
        user = User.objects.create(
            username='testuser1')

        self.assertEqual(user.username, 'testuser1')
        user = User.objects.create(
            username='testuser2')

        self.assertEqual(user.username, 'testuser2')
        self.assertEqual(User.objects.count(), 3)

    def test_tuition_model(self):
        tuition = Tuition.objects.create(
            provider = self.user,
            location = "Narinda",
            phone = "01767374474",
            salary = "7000",
            requirements = "Anyone",
            level = "class 6",
            subject = "English"
        ) 
        self.assertEqual(Tuition.objects.count(), 2)