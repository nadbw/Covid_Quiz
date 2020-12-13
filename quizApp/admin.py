from django.contrib import admin
from quizApp.models import quizUser, Question, Quiz

# Register your models here.
admin.site.register(quizUser)
admin.site.register(Quiz)
admin.site.register(Question)