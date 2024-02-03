from django.urls import path

from .views import index, survey, answer

urlpatterns = [
    path("", index),
    path('<int:pk>', survey, name="survey"),
    path("answer/", answer)
]