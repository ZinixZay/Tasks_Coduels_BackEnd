from django.contrib import admin
from .models import TasksProfile


class TaskProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'avatar', 'backup_email', 'user')
    list_display_links = ('id', 'user')
    search_field = ('user', 'last_name', 'first_name')


admin.site.register(TasksProfile, TaskProfileAdmin)
