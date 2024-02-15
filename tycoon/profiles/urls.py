from django.urls import path, include
from .viewsets import ListTasksProfiles, DetailedTasksProfiles


urlpatterns = [
    path('', ListTasksProfiles.as_view()),
    path('<int:pk>', DetailedTasksProfiles.as_view()),
]

