from django.db import models

from quiz.models import Domain


class RoadmapStep(models.Model):
    """A single step in a learning roadmap for a domain."""
    class Level(models.IntegerChoices):
        FOUNDATIONS = 1, 'Foundations'
        BEGINNER = 2, 'Beginner'
        INTERMEDIATE = 3, 'Intermediate'
        ADVANCED = 4, 'Advanced'
        EXPERT = 5, 'Expert'

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='roadmap_steps')
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField(choices=Level.choices)
    order = models.IntegerField()
    estimated_weeks = models.IntegerField()
    is_milestone = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.domain.name} – {self.title}"
