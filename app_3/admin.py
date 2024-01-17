from django.contrib import admin
from .models import Mode, Title, Content

# Register your models here.


@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'mode', 'brief', 'way']


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['mode', 'title']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'content', 'way']
