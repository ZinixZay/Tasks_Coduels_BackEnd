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
        return Response('meow', status=status.HTTP_200_OK)
