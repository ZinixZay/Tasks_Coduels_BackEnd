from django.urls import path, include
from .viewsets import TasksProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'TasksProfile', TasksProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

