from django.contrib import admin

from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'step', 'resource_type', 'platform', 'is_free', 'difficulty', 'estimated_hours')
    list_filter = ('resource_type', 'is_free', 'difficulty', 'platform')
    search_fields = ('title', 'description', 'platform', 'url')
    list_editable = ('is_free', 'difficulty')
    ordering = ('step', 'resource_type')
