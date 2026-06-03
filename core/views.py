
from django.shortcuts import render
from .models import Question
def home(request):
    return render(request, 'core/home.html')
def question_bank_intro(request):
    topics = [
        ('inequality','نامعادله'),
        ('identity','اتحادها')
    ]
    # صفحه معرفی بانک سوالات (انتخاب موضوع)
    return render(request, 'core/question_bank_intro.html',{'topics': topics})

def question_type(request, topic):
    # صفحه انتخاب نوع سوال برای یک موضوع
    return render(request, 'core/question_type.html', {'topic': topic})

def questions_list(request, topic, qtype):
    # نمایش سوالات همان موضوع و نوع، مرتب شده بر اساس سختی
    questions = Question.objects.filter(topic=topic, qtype=qtype).order_by('difficulty')
    return render(request, 'core/question_list.html', {
        'questions': questions,
        'topic': topic,
        'qtype': qtype
    })


# Create your views here.



