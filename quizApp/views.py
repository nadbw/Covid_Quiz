from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from quizApp.models import quizUser, Quiz, Question

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

def covidQuiz_view(request):
    if request.method == 'POST':
        user = quizUser.objects.create(
            
        )
    return render(request, 'covidQuiz.html', {'user': user})

def dataVis_view(request):
    pass

def createUser_view(request):
    user = quizUser.objects.create_user(
        school=request.POST['School']
    )
    return redirect('covidQuiz_view')