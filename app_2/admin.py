from django.contrib import admin
from .models import Section, Chapter

# Register your models here.


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['headline', 'title', 'content', 'codes']

