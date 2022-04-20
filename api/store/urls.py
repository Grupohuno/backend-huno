from django.contrib import admin
from django.urls import path, include
import store.views as views

urlpatterns = [
    path('dummy/', views.DummyView.as_view()),

]