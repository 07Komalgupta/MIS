from django.core import validators
from django import forms
from django.forms import widgets
from home.models import Student

class AddNewStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        