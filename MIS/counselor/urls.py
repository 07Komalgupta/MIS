from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from .views import AddStudent, HomeView

urlpatterns = [
    path('', login_required(HomeView.as_view()), name="counselorhome"),
    path('addstudent', login_required(AddStudent.as_view()), name="addstudent"),
]
