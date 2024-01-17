from django.contrib import admin
from .models import Chapter, Section

# Register your models here.


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'chapter']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'section', 'content']

