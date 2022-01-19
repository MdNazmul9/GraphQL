from dataclasses import field
import graphene

from graphene_django import DjangoObjectType
from quiz.models import Category, Quizzes, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")



class QuizessType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")
    
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id","question", "answer_text")


class Query(graphene.ObjectType):
    # all_questions = graphene.Field(QuestionType)
    # all_questions = graphene.List(QuestionType)
    all_category = graphene.List(CategoryType)

    def resolve_all_category(self, info):
        return Category.objects.all()
schema = graphene.Schema(query=Query)