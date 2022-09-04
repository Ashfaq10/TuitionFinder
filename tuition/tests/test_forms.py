from django.test import TestCase
from tuition.models.tuiton_models import Tuition
from tuition.models.users_models import User

from tuition.utils.tuition_forms import TuitionModelForm

class TestForms(TestCase):

    def test_tuition_form_valid(self):

            form = TuitionModelForm({
                "location":"Dhanmondi",
                "level":"class 5",
                "subject":"Math",
                "requirements":"Anyone",
                "salary":"5000",
                "phone": "1231543534",
            })
            print(form.errors)
            self.assertTrue(form.is_valid())

    def test_tuition_form_invalid(self):
        form =TuitionModelForm({
        })
        self.assertFalse(form.is_valid())
        