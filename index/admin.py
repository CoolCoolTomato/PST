from django.contrib import admin
from .models import Notice, Feedback

# Register your models here.


@admin.register(Notice)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'times']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'kind', 'contact', 'content']

