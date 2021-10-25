from django.contrib.auth.models import User
from django.db import models


class Part(models.Model):
    id = models.CharField(max_length=20, verbose_name='Название отделения',
                          primary_key=True, unique=True)
    full_name = models.CharField(max_length=200,
                                verbose_name='Полное название')
    description = models.TextField(verbose_name='Описание', blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return f'{self.id} - {self.full_name}'


class Group(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    course = models.IntegerField(verbose_name='Курс')
    fk_part = models.ForeignKey(Part, on_delete=models.CASCADE,
                                verbose_name='Отделение')
    mtm_user = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    code = models.CharField(max_length=20, verbose_name='Код')
    semester = models.IntegerField(verbose_name='Номер семестра')
    hours = models.FloatField(verbose_name='Часы')

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name


class EducatorDiscipline(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподаватель')
    fk_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплина')

    class Meta:
        verbose_name = 'Распределение дисциплины'
        verbose_name_plural = 'Распределение дисциплин'

    def __str__(self):
        return f'{self.fk_user} - {self.fk_discipline}'


class Territory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    address = models.CharField(max_length=200, verbose_name='Адресс')

    class Meta:
        verbose_name = 'Территория'
        verbose_name_plural = 'Территории'

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название кабинета')
    number = models.CharField(max_length=15, verbose_name='Номер кабинета')
    fk_territoty = models.ForeignKey(Territory, on_delete=models.CASCADE, verbose_name='Название территории')

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self):
        return f'{self.number} - {self.fk_territoty}'


class DisciplineOnGroup(models.Model):
    fk_edu_dis = models.ForeignKey(EducatorDiscipline, on_delete=models.CASCADE)
    fk_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    fk_cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return f'{self.fk_group} - {self.fk_edu_dis} - {self.fk_cabinet}'

