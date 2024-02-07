from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


class Survey(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(max_length=200)
    content = HTMLField(blank=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    content = HTMLField(blank=True)
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
            related_name="answers",
            null=True, blank=True,
            )
    next_question = models.OneToOneField(
        Question,
            on_delete=models.CASCADE,
            related_name="previous_answer",
            null=True, blank=True,
            )

    def __str__(self):
        return self.content


class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='users_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.name
