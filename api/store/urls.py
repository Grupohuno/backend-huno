from django.contrib import admin
from django.urls import path, include
from .views import DummyView

urlpatterns = [
    path('dummy/', DummyView.as_view()),

]