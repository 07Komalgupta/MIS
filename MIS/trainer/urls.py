from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="trainerhome"),
]
