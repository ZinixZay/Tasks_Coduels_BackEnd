from django.urls import include, path
from rest_framework import routers

import exercises.viewsets as viewsets

router = routers.DefaultRouter()
router.register(r'exercises', viewsets.ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
