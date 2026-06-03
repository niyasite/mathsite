from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('<int:topic_id>/<int:step_order>/', views.step_view, name='step_view'),
]