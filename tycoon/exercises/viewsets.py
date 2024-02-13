from .models import Exercise, Question, Answer
from rest_framework import permissions, viewsets

from .serializers import ExerciseSerializer, QuestionSerializer, AnswerSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly, )
