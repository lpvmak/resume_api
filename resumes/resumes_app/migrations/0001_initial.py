# Generated by Django 4.2.2 on 2023-06-19 22:47

import django.core.validators
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('title', models.CharField(max_length=128,
                                           verbose_name='Название резюме')),
                ('status', models.CharField(
                    choices=[('draft', 'Черновик'), ('active', 'Активно'),
                             ('archive', 'В архиве')], default='d',
                    max_length=7, verbose_name='Статус')),
                ('grade', models.CharField(max_length=64,
                                           verbose_name='Уровень квалификации')),
                ('specialty', models.CharField(max_length=64,
                                               verbose_name='Специальность')),
                ('salary',
                 models.PositiveIntegerField(verbose_name='Ожидаемый доход')),
                ('education', models.TextField(blank=True, default='',
                                               verbose_name='Образование')),
                ('experience', models.TextField(blank=True, default='',
                                                verbose_name='Опыт работы')),
                ('portfolio', models.TextField(blank=True, default='',
                                               verbose_name='Портфолио')),
                ('phone',
                 models.CharField(blank=True, default='', max_length=12,
                                  validators=[
                                      django.core.validators.RegexValidator(
                                          message='Номер телефона должен начинаться с + и содержать от 8 до 12 цифр',
                                          regex='\\+\\d{8,12}')],
                                  verbose_name='Номер телефона')),
                ('email',
                 models.EmailField(blank=True, default='', max_length=254)),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='resumes',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Владелец')),
            ],
            managers=[
                ('api_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
