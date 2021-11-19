from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from .views import HomeView, AddCourse

urlpatterns = [
    path('', login_required(HomeView.as_view()), name="centerheadhome"),
    path('addcourse/', login_required(AddCourse.as_view()), name="addcourse"),
]
