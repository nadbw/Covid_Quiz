from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class quizUser(models.Model):
    class pennSchool(models.TextChoices):
        SAS = 'SAS', _('SAS')
        SEAS = 'SEAS', _('SEAS')
        NURS = 'NURS', _('Nursing')
        WHAR = 'WHAR', _('Wharton')
        GRAD = 'GRAD', _('Graduate')
        DEFAULT = 'DEFAULT', _('Default')
    school = models.CharField(
        max_length=10,
        choices=pennSchool.choices,
        default=pennSchool.DEFAULT
    )

    # class YearInSchool(models.TextChoices):
    #     FRESHMAN = 'FR', _('Freshman')
    #     SOPHOMORE = 'SO', _('Sophomore')
    #     JUNIOR = 'JR', _('Junior')
    #     SENIOR = 'SR', _('Senior')
    #     GRADUATE = 'GR', _('Graduate')

    # year_in_school = models.CharField(
    #     max_length=2,
    #     choices=YearInSchool.choices,
    #     default=YearInSchool.FRESHMAN
    # )
    
    # covidScore = models.IntegerField(default=0)
    # quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, default=1)
    # isOnCampus = models.BooleanField(default=False)
    #implement more specific location field

class Question(models.Model):
    class Answer(models.TextChoices):
        NEVER = 'NEVER', _('Never')
        ONCE_PM = 'ONCE_PM', _('Once/few times per month')
        ONCE_PW = 'ONCE_PW', _('Once/few times per week')
        EVERYDAY = 'EVERYDAY', _('Everyday')

    answer = models.CharField(
        max_length=10,
        choices=Answer.choices,
        default=Answer.NEVER
    )
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    body = models.CharField(max_length=200, default="Default Question")
    user = models.ForeignKey('quizUser', on_delete=models.CASCADE, default=1)