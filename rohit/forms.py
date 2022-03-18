import imp
from django.forms import ModelForm
from rohit import models


class create_person_form(ModelForm):
    class Meta:
        model = models.Person
        fields = "__all__"