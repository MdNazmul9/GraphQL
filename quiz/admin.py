from django.contrib import admin
from .models import Category, Quizzes, Question, Answer
admin.site.register([Category, Quizzes, Question, Answer])