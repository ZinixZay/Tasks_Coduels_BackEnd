from django.contrib import admin
from .models import Exercise, Question, Answer


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'identifier', 'creator')
    list_display_links = ('id', 'title', 'identifier')
    search_fields = ('title', 'identifier')
    list_filter = ('is_feedback', )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise', 'label', 'question_type')
    list_display_links = ('id', )
    search_fields = ('exercise', 'term')
    list_filter = ('question_type', )


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question')
    list_display_links = ('id', )
    search_fields = ('user', 'question')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
