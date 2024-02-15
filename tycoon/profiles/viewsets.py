from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TasksProfile
from .serializers import TasksProfileSerializer


class ListTasksProfiles(APIView):

    def get(self, request):
        tasks_profiles = [tasks_profile.to_dict() for tasks_profile in TasksProfile.objects.all()]
        return Response(tasks_profiles)
