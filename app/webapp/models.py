from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    ACTIVE = 'active', 'Активна'
    BLOCKED = 'blocked', 'Заблокировано'


class Note(models.Model):
    author = models.CharField(max_length=150, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=2500, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    status = models.CharField(choices=StatusChoices.choices, max_length=100, null=False, blank=False,
                              default=StatusChoices.ACTIVE, verbose_name='Статус')

    def __str__(self):
        return f'Автор: {self.author}, Статус: {self.get_status_display()}, Дата создания: {self.created_at}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
