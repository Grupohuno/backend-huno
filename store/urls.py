from django.urls import path
from .views import DummyView

urlpatterns = [
    path("dummy/", DummyView.as_view()),
]
