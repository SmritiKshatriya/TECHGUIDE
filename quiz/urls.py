from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    
    
    # Auth Routes
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]