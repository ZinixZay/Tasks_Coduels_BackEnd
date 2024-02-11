from django.db import models
from django.utils import timezone

import autoslug

from .utils import generate_identifier

from users.models import CustomUser

# Create your models here.


class Exercise(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=127)
    brief_description = models.CharField(verbose_name='Краткое описание', max_length=255)
    detailed_description = models.TextField(verbose_name='Полное описание', blank=True)
    is_feedback = models.BooleanField(verbose_name='Показывать результат', default=True)
    attempts = models.IntegerField(verbose_name='Количество попыток', default=1)
    attachment = models.FileField(verbose_name='Приложение', upload_to="uploads/%Y/%m/%d/", blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    slug = autoslug.AutoSlugField(verbose_name='URL', max_length=255, unique=True, db_index=True, populate_from=title)
    identifier = models.CharField(verbose_name='Идентификатор', unique=True, db_index=True,
                                  default=generate_identifier, max_length=7)
    creator = models.ForeignKey(CustomUser, verbose_name='Создатель', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title + self.identifier)

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
        ordering = ['date_created']


class Question(models.Model):
    QUESTION_TYPES = {
        'radio': 'С одним ответом',
        'checkbox': 'С несколькими ответами',
        'consistency': 'С развернутым ответом (автоматическая проверка)',
        'textarea': 'С развернутым ответом (ручная проверка)',
    }

    label = models.CharField(verbose_name='Порядковый номер вопроса', max_length=3)
    question_type = models.CharField(verbose_name='Тип вопроса', max_length=15, choices=QUESTION_TYPES)
    term = models.CharField(verbose_name='Содержание', max_length=255)
    content = models.JSONField(verbose_name='Контент')
    exercise = models.ForeignKey(Exercise, verbose_name='Задание', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exercise.title + self.label)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['exercise']


class Answer(models.Model):
    content = models.JSONField(verbose_name='Контент')
    user = models.ForeignKey(CustomUser, verbose_name='Отвечающий', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.email + self.question.label + self.question.exercise.title)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['user', 'question']
