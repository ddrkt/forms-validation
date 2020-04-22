from django.contrib import admin
from django.urls import path, include
from forms import views
from django.views.generic import TemplateView


urlpatterns = [
    path('values/', views.FormViewSet.as_view()),
]
