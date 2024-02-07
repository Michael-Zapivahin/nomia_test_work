
from .models import Survey, Question, Answer
from more_itertools import chunked
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.models import User


def index(request):
    surveys = Survey.objects.all()
    context = {
        'page_columns': list(chunked(surveys, 1)),
    }
    return render(request, template_name='index.html', context=context)


def survey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    context = {
        'questions': survey.questions.all().order_by('pk'),
    }
    return render(request, 'feedbackForm.html', context=context)


def answer(request):
    counter = Question.objects.count()+1
    user_name = request.POST.get("user_name")
    user_mail = request.POST.get("user_mail")
    user = User.objects.filter(username=user_mail).first()
    if not user:
        user, created = User.objects.get_or_create(first_name=user_name, username=user_mail, email=user_mail)
    answers = []
    survey_name = None
    for key in range(1, counter):
        answer = request.POST.get(f"answer{key}")
        if answer != None:
            question = get_object_or_404(Question, pk=key)
            if not survey_name:
                survey_name = question.survey.name

            response = Answer.objects.create(
                user=user,
                question=question,
                content=answer,
            )
            answers.append({
                'question': response.question.content,
                'answer': answer.content,
            })

    context = {
        'user_name': user.name,
        'answers': answers,
        'survey_name': survey_name,
    }
    return render(request, 'survey_result.html', context=context)
    # return HttpResponsePermanentRedirect("/")


def survey_result(request, content):
    pass