

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models.mixins import InfoMixin

User = get_user_model()


class Organization(InfoMixin):
    name = models.CharField('Название', max_length=255)
    director = models.ForeignKey(
        User, models.RESTRICT, 'organisations_directors',
        verbose_name='Директор'
    )
    employees = models.ManyToManyField(
        User, "organizations_employees", verbose_name="Сотрудники",
        blank=True, through='Employee'
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name', 'id',)

    def __str__(self):
        return f"{self.name} ({self.pk})"



class Employee(models.Model):
    organization = models.ForeignKey(
        'Organization', models.CASCADE, 'employees_info',
    )
    user = models.ForeignKey(
        User, models.CASCADE, 'organizations_info',
    )
    position = models.ForeignKey(
        'Position', models.RESTRICT, 'employees',
    )
    date_joined = models.DateField('Date joined', default=timezone.now)

    class Meta:
        verbose_name = 'Сотрудник организации'
        verbose_name_plural = 'Сотрудники организаций'
        ordering = ('-date_joined',)
        unique_together = (('organization', 'user'),)

    def __str__(self):
        return f'Employee #{self.pk} {self.user}'