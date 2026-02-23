from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Domain(models.Model):
    """Tech domain/career area (e.g. Web Dev, Data Science)."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon_emoji = models.CharField(max_length=10)
    color_hex = models.CharField(max_length=7)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class QuizQuestion(models.Model):
    """A single question in the career quiz."""
    class Category(models.TextChoices):
        TECHNICAL = 'TECHNICAL', 'Technical'
        CREATIVE = 'CREATIVE', 'Creative'
        INTEREST = 'INTEREST', 'Interest'
        WORKSTYLE = 'WORKSTYLE', 'Work Style'
        CAREER = 'CAREER', 'Career'

    question_text = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices)
    order = models.IntegerField()

    def __str__(self):
        return self.question_text[:50] + ('...' if len(self.question_text) > 50 else '')


class QuizChoice(models.Model):
    """One possible answer to a quiz question."""
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.question_id}: {self.choice_text[:40]}{'...' if len(self.choice_text) > 40 else ''}"


class ChoiceDomainScore(models.Model):
    """How much a given choice contributes to a domain (for scoring)."""
    choice = models.ForeignKey(QuizChoice, on_delete=models.CASCADE, related_name='domain_scores')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='choice_scores')
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['choice', 'domain'], name='unique_choice_domain'),
        ]

    def __str__(self):
        return f"{self.choice} → {self.domain}: {self.score}"
