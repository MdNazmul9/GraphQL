from unicodedata import category
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model): # Admission, GOV JOB, BPSC, IT, NON Technical
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Quizzes(models.Model): # ICT, Math, Bangla, English etc
    title = models.CharField(max_length=255, default=_("New Quizz"))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class Question(models.Model): # Main Question, WH Question
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advance')),
        (4, _('Expert'))

    )
    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(Quizzes, related_name="questions", on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return  self.title

class Answer(models.Model): # options and select right option
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.DO_NOTHING) # which question option it is???
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False) # which option is right

    def __str__(self):
        return self.answer_text
