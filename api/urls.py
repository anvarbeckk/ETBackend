from django.urls import path
from api.views import QuestionList


urlpatterns = [
    path('api/v1/questions', QuestionList.as_view(), name='question-list'),
]