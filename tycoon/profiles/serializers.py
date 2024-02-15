from rest_framework import serializers
from .models import TasksProfile


class TasksProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksProfile
        fields = ('id', 'user', 'status', 'first_name', 'last_name', 'middle_name', 'avatar', 'backup_email', 'slug')
