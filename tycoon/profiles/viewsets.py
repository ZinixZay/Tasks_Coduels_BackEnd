from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TasksProfile
from .serializers import TasksProfileSerializer


class ListTasksProfiles(APIView):

    def get(self, request):
        tasks_profiles = [tasks_profile.to_dict() for tasks_profile in TasksProfile.objects.all()]
        return Response(tasks_profiles, status=200)


class DetailedTasksProfiles(APIView):

    def get(self, request, pk):
        tasks_profile = TasksProfile.objects.filter(pk=pk)
        if tasks_profile:
            return Response(tasks_profile[0].to_dict(), status=200)
        return Response({"error": f"user with id {pk} not found"}, status=404)

    def patch(self, request, pk):
        tasks_profile = TasksProfile.objects.filter(pk=pk)
        if tasks_profile:
            serializer = TasksProfileSerializer(tasks_profile[0], data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(tasks_profile[0].to_dict(), status=201)
            else:
                return Response({"error": f"wrong parameters"}, status=400)
        return Response({"error": f"user with id {pk} not found"}, status=400)

