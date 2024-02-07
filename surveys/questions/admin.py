from django.contrib import admin
from .models import (
    Survey,
    Question,
    Answer,
)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    ordering = ['name']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'next_question']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']


# @admin.register(Answer)
# class AnswerInLine(admin.TabularInline):
#     model = Answer
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['survey', 'name']
#     inlines = [AnswerInLine]
