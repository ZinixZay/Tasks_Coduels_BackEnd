from django.urls import path, include
from .viewsets import ListTasksProfiles


urlpatterns = [
    path('', ListTasksProfiles.as_view()),
]

