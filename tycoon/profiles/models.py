from django.db import models
from users.models import CustomUser

import autoslug


class TasksProfile(models.Model):
    STATUSES = {
        'teacher': 'Преподаватель',
        'student': 'Ученик'
    }
    first_name = models.CharField(verbose_name='Имя', max_length=31, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=31, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=31, blank=True)
    status = models.CharField(verbose_name='Статус', max_length=15, choices=STATUSES, default='student')
    backup_email = models.EmailField(verbose_name='Резервная почта', blank=True)
    avatar = models.ImageField(verbose_name='Фото', upload_to='avatars/%Y/%m/%d/', blank=True)
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    slug = autoslug.AutoSlugField(verbose_name='URL', max_length=255, unique=True,
                                  db_index=True, populate_from='last_name')

    def __str__(self):
        return str(self.user.email + self.last_name + self.first_name)

    class Meta:
        verbose_name = 'Профиль(Задания)'
        verbose_name_plural = 'Профили(Задания)'
        ordering = ['last_name']


