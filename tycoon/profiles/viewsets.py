from rest_framework import permissions, viewsets
from .models import TasksProfile
from .serializers import TasksProfileSerializer


class TasksProfileViewSet(viewsets.ModelViewSet):
    queryset = TasksProfile.objects.all()
    serializer_class = TasksProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
