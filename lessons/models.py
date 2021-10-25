from django.contrib.auth.models import User
from django.db import models

from training_department.models import DisciplineOnGroup


class Lesson(models.Model):
    CHECK_CHOICES = (
        ('', 'На месте'),
        ('н/б', 'Не был'),
        ('н/бу', 'Не был по уважительной причине'),
    )
    MARK_CHOICES = (
        ('5', 'Отлично'),
        ('4', 'Хорошо'),
        ('3', 'Удовлетворительно'),
        ('2', 'Не удовлетворительно'),
        ('', 'Нет оценки'),
    )

    fk_dis_on_group = models.ForeignKey(DisciplineOnGroup, on_delete=models.CASCADE, verbose_name='Занятие')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Студент')
    check = models.CharField(max_length=40, choices=CHECK_CHOICES, default='', verbose_name='Присутствие')
    mark = models.CharField(max_length=20, choices=MARK_CHOICES, default='', verbose_name='Присутствие')

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return f'{self.fk_dis_on_group}, {self.fk_user} - {self.mark}, {self.check}'








