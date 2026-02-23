from rest_framework import serializers
from .models import RoadmapStep
from resources.models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id', 'title', 'url', 'resource_type',
            'platform', 'is_free', 'difficulty',
            'estimated_hours', 'description'
        ]


class RoadmapStepSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = RoadmapStep
        fields = [
            'id', 'title', 'description', 'level',
            'order', 'estimated_weeks', 'is_milestone',
            'resources'
        ]