from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from .models import TasksProfile
from .serializers import TasksProfileSerializer


class TasksProfileViewSet(viewsets.ModelViewSet):
    queryset = TasksProfile.objects.all()
    serializer_class = TasksProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def list(self, request):
        return Response(self.serializer_class(self.queryset, many=True).data,
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        TasksProfile.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            middle_name=request.data['middle_name'],
            backup_email=request.data['backup_email'],
            user=request.user
        )
        return Response('meow', status=status.HTTP_200_OK)
