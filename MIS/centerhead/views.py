from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, FormView, CreateView
from home.models import Student
from .forms import AddNewCourse

# Create your views here.

# @login_required(login_url='login')
class HomeView(TemplateView):
    template_name = "centerhead/centerheadhome.html"


class AddCourse(TemplateView):
    template_name = "centerhead/addnewcourse.html"
    
    def post(self,rerquest, *args, **kwargs):
        fm = AddNewCourse(self.request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = AddNewCourse()
        stu = Student.objects.all()
        context = {'student': stu, 'form': fm}
        return context
