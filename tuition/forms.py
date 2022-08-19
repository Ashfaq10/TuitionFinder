from ast import ImportFrom
from django.forms import ModelForm
from tuition.models import Tuition

class TuitionModelForm(ModelForm):
    class Meta:
        model = Tuition
        fields = '__all__'