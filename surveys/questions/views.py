
from .models import Survey, Question, Response
from more_itertools import chunked
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    answers =[]
    user_name = request.POST.get("user_name")
    user_mail = request.POST.get("user_mail")
    user, created = User.objects.get_or_create(first_name=user_name, username=user_mail, email=user_mail)
    for key in range(1, counter):
        answer = request.POST.get(f"answer{key}")
        if answer != None:
            Response.objects.create(
                user=user,
                question=get_object_or_404(Question, pk=key),
                content=answers,
            )
            answers.append({
                'question_id': key,
                'answer': answer,
            })

    return HttpResponse(f"<h2>user {user_name} answers: {answers} </h2>")
