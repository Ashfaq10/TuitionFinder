from ast import ImportFrom
from django.forms import ModelForm
from tuition.models.tuiton_models import Tuition

class TuitionModelForm(ModelForm):
    class Meta:
        model = Tuition
        exclude = ['provider']



