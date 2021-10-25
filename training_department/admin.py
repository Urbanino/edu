from django.contrib import admin
from .models import *


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    class Meta:
        model = Discipline

    list_display = ('name', 'code', 'semester', 'hours', )
    list_filter = ('code', 'semester',)


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    class Meta:
        model = Part

    list_display = ('id', 'full_name', 'description', )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    class Meta:
        model = Group

    list_display = ('name', 'course', 'fk_part',)
    list_filter = ('fk_part', 'course',)


@admin.register(EducatorDiscipline)
class EducatorDisciplineAdmin(admin.ModelAdmin):
    class Meta:
        model = EducatorDiscipline

    list_display = ('fk_user', 'fk_discipline', )
    list_filter = ('fk_user', 'fk_discipline', )


@admin.register(Territory)
class TerritoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Territory

    list_display = ('name', 'address', )
