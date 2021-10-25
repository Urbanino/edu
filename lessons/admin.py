from django.contrib import admin
from .models import *


@admin.register(Lesson)
class DisciplineAdmin(admin.ModelAdmin):
    class Meta:
        model = Lesson

    list_display = ('fk_dis_on_group', 'fk_user', 'check', 'mark', )

