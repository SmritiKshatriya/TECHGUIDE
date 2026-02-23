from django.db import models

from roadmaps.models import RoadmapStep


class Resource(models.Model):
    """A learning resource (video, article, course, etc.) linked to a roadmap step."""
    class ResourceType(models.TextChoices):
        VIDEO = 'VIDEO', 'Video'
        ARTICLE = 'ARTICLE', 'Article'
        COURSE = 'COURSE', 'Course'
        BOOK = 'BOOK', 'Book'
        INTERACTIVE = 'INTERACTIVE', 'Interactive'
        PROJECT = 'PROJECT', 'Project'

    class Difficulty(models.TextChoices):
        BEGINNER = 'BEGINNER', 'Beginner'
        INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
        ADVANCED = 'ADVANCED', 'Advanced'

    step = models.ForeignKey(RoadmapStep, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=300)
    url = models.URLField()
    resource_type = models.CharField(max_length=20, choices=ResourceType.choices)
    platform = models.CharField(max_length=100)
    is_free = models.BooleanField()
    difficulty = models.CharField(max_length=20, choices=Difficulty.choices)
    estimated_hours = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
