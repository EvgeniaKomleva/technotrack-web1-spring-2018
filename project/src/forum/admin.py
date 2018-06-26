from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = 'name', 'author'
    search_fields = 'name', 'author__username'
