# Generated by Django 3.1.3 on 2020-12-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='body',
            field=models.CharField(default='Default Question', max_length=200),
        ),
    ]
