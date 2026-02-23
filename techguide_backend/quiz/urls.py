from django.urls import path

from .views import QuizQuestionsAPIView, SubmitQuizAPIView

app_name = 'quiz'

urlpatterns = [
    path('', QuizQuestionsAPIView.as_view(), name='questions'),
    path('questions/', QuizQuestionsAPIView.as_view(), name='questions-list'),
    path('submit/', SubmitQuizAPIView.as_view(), name='submit'),
]
