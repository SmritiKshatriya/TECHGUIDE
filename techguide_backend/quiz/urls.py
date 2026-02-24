from django.urls import path
from .views import QuizQuestionsAPIView, SubmitQuizAPIView, DomainsListAPIView

urlpatterns = [
    path('questions/', QuizQuestionsAPIView.as_view()),
    path('submit/', SubmitQuizAPIView.as_view()),
    path('domains/', DomainsListAPIView.as_view()),
]