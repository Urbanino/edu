from django.contrib import admin
from .models import *


@admin.register(Equipment)
class DisciplineAdmin(admin.ModelAdmin):
    class Meta:
        model = Equipment

    list_display = ('name', 'model', 'code', 'fk_cabinet')
    list_filter = ('model', 'fk_cabinet',)
