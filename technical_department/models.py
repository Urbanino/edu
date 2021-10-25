from django.db import models
from training_department.models import Cabinet


class Equipment(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название оборудования')
    model = models.CharField(max_length=200, verbose_name='Модель оборудования')
    code = models.CharField(max_length=255, verbose_name='Инвентарный номер')
    fk_cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name='Расположение оборудования')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return f'{self.model} - {self.code}'
