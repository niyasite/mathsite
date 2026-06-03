from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.question_bank_intro, name='question_bank_intro'),
    path('questions/<str:topic>/', views.question_type, name='question_type'),
    path('questions/<str:topic>/<str:qtype>/', views.questions_list, name='questions_list'),
]
