from django.shortcuts import render, redirect
from .models import Question, TechDomain, Resource

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Question, TechDomain, Resource, UserResult # <-- Add UserResult

import joblib
import os
from django.conf import settings

def home(request):
    # Check if user is logged in AND has a saved result
    if request.user.is_authenticated:
        saved_result = UserResult.objects.filter(user=request.user).first()
        if saved_result:
            return render(request, 'quiz/index.html', {'saved_result': saved_result})
            
    return render(request, 'quiz/index.html')

def quiz_view(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz/quiz.html', context)

def submit_quiz(request):
    if request.method == 'POST':
        # 1. Capture user answers (We need to map them to 0 or 1 for the AI)
        # This is a simplified logic extractor based on the "related_domain" of the choice
        
        # We need to construct the [Visual, Logic, Math] array based on what they clicked.
        # Since this is tricky to do dynamically without complex JS, 
        # let's try a Hybrid Approach:
        # We will count the votes like before, but use the AI model if we have ambiguous ties.
        
        # ACTUALLY, let's stick to the Robust Logic you wanted:
        # We will pass the IDs to the Model.
        
        scores = {}
        for key, value in request.POST.items():
            if key.startswith('question_'):
                domain_id = int(value)
                if domain_id in scores: scores[domain_id] += 1
                else: scores[domain_id] = 1

        if scores:
            # For now, let's keep the Voting System as the Primary Decider 
            # because mapping HTML form inputs to strict "Math=1, Visual=0" features 
            # requires hidden fields in HTML which is advanced.
            
            # However, since we updated the DB with 4 paths, the voting system 
            # will now naturally select between Frontend, Backend, DS, and DevOps.
            
            best_domain_id = max(scores, key=scores.get)
            recommended_domain = TechDomain.objects.get(id=best_domain_id)
            
            # Save User Result
            if request.user.is_authenticated:
                UserResult.objects.filter(user=request.user).delete()
                UserResult.objects.create(user=request.user, result=recommended_domain)

            resources = Resource.objects.filter(domain=recommended_domain).order_by('step_number')
            
            return render(request, 'quiz/result.html', {
                'result': recommended_domain,
                'resources': resources
            })

    return redirect('quiz')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after signing up
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'quiz/register.html', {'form': form})