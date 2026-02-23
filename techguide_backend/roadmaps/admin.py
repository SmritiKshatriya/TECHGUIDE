from django.contrib import admin

from .models import RoadmapStep


@admin.register(RoadmapStep)
class RoadmapStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'domain', 'level', 'order', 'estimated_weeks', 'is_milestone')
    list_filter = ('domain', 'level', 'is_milestone')
    search_fields = ('title', 'description')
    list_select_related = True
    ordering = ('domain', 'level', 'order')
