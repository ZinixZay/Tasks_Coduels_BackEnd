from .models import Exercise, Question, Answer
from rest_framework import serializers


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'title', 'identifier', 'creator', 'brief_description', 'detailed_description', 'is_feedback', 'attempts',
                  'attachment', 'date_created', 'slug')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('exercise', 'label', 'term', 'question_type', 'content')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('user', 'question', 'content')
