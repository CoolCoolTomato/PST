from django.contrib import admin
from .models import Titles, Contents
# Register your models here.


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ['headline', 'name', 'content']

