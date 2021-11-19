from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from home.models import Student
from .forms import AddNewStudent

# Create your views here.

# @login_required(login_url='login')
class HomeView(TemplateView):
    template_name = "counselor/counselorhome.html"


class AddStudent(TemplateView):
    template_name = "counselor/addstudent.html"
    
    def post(self,rerquest):
        fm = AddNewStudent(request.POST)
        if fm.is_valid():
            pass

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = AddNewStudent()
        stu = Student.objects.all()
        context = {'student': stu, 'form': fm}
        return context
