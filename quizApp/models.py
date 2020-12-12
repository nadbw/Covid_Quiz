from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=200)
    covidScore = models.IntegerField()
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    body = models.CharField(max_length=200, default="Default Question")

    class Answer(models.IntegerChoices):
            NEVER = 0
            EVERY_MONTH = 1
            EVERY_WEEK = 2
            EVERY_DAY = 3

    answer = models.IntegerField(choices=Answer.choices)