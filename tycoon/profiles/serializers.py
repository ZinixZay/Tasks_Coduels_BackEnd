from rest_framework import serializers
from .models import TasksProfile


class TasksProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksProfile
        fields = ('user', 'first_name', 'last_name', 'middle_name', 'avatar', 'backup_email')
