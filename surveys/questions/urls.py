from django.urls import path

from .views import index, survey, answer, survey_result

urlpatterns = [
    path("", index),
    path('<int:pk>', survey, name="survey"),
    path("answer/", answer),
]
