from django.shortcuts import render, redirect, get_object_or_404
from quizApp.models import quizUser, Quiz, Question

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})

def covidQuiz_view(request):
    # will only write questions if a user is made --- change later?? not super safe
    if request.method == 'POST':
        user = quizUser.objects.create(
            school=request.POST['School'],
            year_in_school=request.POST['Year'],
            quiz=Quiz.objects.get(title="Covid Quiz")
        )
        # clear questions for new user, write covid quiz questions, store in questions
        Question.objects.filter(quiz__title="Covid Quiz").delete()
        write_covidQuiz_questions(user.id)
        questions = Question.objects.filter(quiz__title="Covid Quiz")
        
    args = {'user':user, 'questions':questions}
    return render(request, 'covidQuiz.html', args)

def dataVis_view(request):
    return render(request, 'dataVis.html')

def write_covidQuiz_questions(userID):
    currUser = quizUser.objects.get(id=userID)
    covidQuiz = Quiz.objects.get(title="Covid Quiz")
    
    q1 = Question.objects.create(
        quiz=covidQuiz,
        body="How often do you eat in a restaurant outside",
    )