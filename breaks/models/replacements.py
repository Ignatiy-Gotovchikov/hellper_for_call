from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        User, models.CASCADE, "replacements",
        verbose_name="Сотрудник"
    )
    replacements = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'employees',
        verbose_name="Смена"
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', models.RESTRICT, 'replacements_employees',
        verbose_name="Статус"
    )


    class Meta:
        verbose_name = "Смена - Работник"
        verbose_name_plural = "Смены - Работники"

    def __str__(self):
        return f"Смена {self.replacements} для {self.employee}"


class ReplacementStatus(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=True)


    class Meta:
        verbose_name = "Статус смены"
        verbose_name_plural = "Статусы смены"
        ordering = ("sort",)

    def __str__(self):
        return f"{self.code} для {self.name}"

class Replacement(models.Model):
    group = models.ForeignKey(
        to='breaks.Group', on_delete=models.CASCADE, related_name="replacements",
        verbose_name="Группа"
    )
    date = models.DateField('Дата смены')
    break_start = models.TimeField('Начало обеда')
    break_end = models.TimeField('Конец обеда')
    break_max_duration = models.PositiveSmallIntegerField('Макс. продолжительность обеда', null=True, blank=True)

    class Meta:
        verbose_name = "Смена"
        verbose_name_plural = "Смены"
        ordering = ("-date",)

    def __str__(self):
        return f"Смена №{self.pk} для {self.group}"


