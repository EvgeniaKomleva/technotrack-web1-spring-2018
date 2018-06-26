from django.contrib import admin
from .models import Training


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = 'name', 'trainer', 'data'
    search_fields = 'name', 'trainer__username', 'data'
