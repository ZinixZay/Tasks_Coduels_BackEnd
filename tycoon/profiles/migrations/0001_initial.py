# Generated by Django 5.0.1 on 2024-02-01 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=31, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=31, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=31, verbose_name='Отчество')),
                ('backup_email', models.EmailField(blank=True, max_length=254, verbose_name='Резервная почта')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/%Y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['last_name'],
            },
        ),
    ]
