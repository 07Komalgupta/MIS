from django.core import validators
from django import forms
from django.forms import widgets
from home.models import Course

class AddNewCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            fields: forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
        }
        