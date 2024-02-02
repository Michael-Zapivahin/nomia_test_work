from django.contrib import admin
from django import forms
from .models import Survey, Question, Response


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    ordering = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['survey', 'name', 'content']


# @admin.register(Response)
# class ResponseAdmin(admin.ModelAdmin):
#     pass
    # list_display = ['user', 'question']

