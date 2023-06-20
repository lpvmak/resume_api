from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q, Manager


class ResumeStatusChoices(models.TextChoices):
    draft = 'draft', 'Черновик'
    active = 'active', 'Активно'
    archive = 'archive', 'В архиве'


class ApiResumeManager(models.Manager):
    """
    Кастомный менеджер Resume для api
    Всем доступны активные резюме
    Владельцу доступны также все его резюме
    """

    def public(self):
        return super().get_queryset().filter(status='active')

    def private(self, user):
        return super().get_queryset().filter(Q(status='active') | Q(user=user))


class Resume(models.Model):
    """
    Модель Резюме
    """

    user = models.ForeignKey(
        get_user_model(),
        related_name='resumes',
        verbose_name='Владелец',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=128,
        blank=False,
        verbose_name="Название резюме"
    )
    status = models.CharField(
        max_length=7,
        choices=ResumeStatusChoices.choices,
        default=ResumeStatusChoices.draft.value[0],
        verbose_name='Статус'
    )
    grade = models.CharField(
        max_length=64,
        verbose_name='Уровень квалификации'
    )
    specialty = models.CharField(max_length=64, verbose_name='Специальность')
    salary = models.PositiveIntegerField(verbose_name='Ожидаемый доход')
    education = models.TextField(
        null=False,
        default="",
        blank=True,
        verbose_name="Образование"
    )
    experience = models.TextField(
        null=False,
        default="",
        blank=True,
        verbose_name="Опыт работы"
    )
    portfolio = models.TextField(
        null=False,
        default="",
        blank=True,
        verbose_name="Портфолио"
    )
    phone = models.CharField(
        max_length=12,
        validators=(
            RegexValidator(
                regex=r"\+\d{8,12}",
                message="Номер телефона должен начинаться с + и содержать от 8 до 12 цифр"
            ),
        ),
        verbose_name="Номер телефона",
        blank=True,
        default=""
    )
    email = models.EmailField(
        blank=True,  # Необязательное поле в админ панеле
        default=""
    )

    objects = Manager()
    api_objects = ApiResumeManager()
