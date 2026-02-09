from django.db import models
from django.contrib.auth.models import User

# 1. The Result Categories (e.g., Frontend, Backend)
class TechDomain(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Frontend Development"
    description = models.TextField()         # e.g., "You love visual..."

    def __str__(self):
        return self.name

# 2. The Questions
class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

# 3. The Choices for each Question
class Choice(models.Model):
    # Link this choice to a specific Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    # If the user picks this choice, which Domain does it point to?
    # This acts as our "Simple AI" logic mapping.
    related_domain = models.ForeignKey(TechDomain, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

# 4. The Roadmap Resources
class Resource(models.Model):
    RESOURCE_TYPES = (
        ('Video', 'Video'),
        ('Article', 'Article/Documentation'),
        ('Course', 'Course'),
    )
    COST_TYPES = (
        ('Free', 'Free'),
        ('Paid', 'Paid'),
    )

    domain = models.ForeignKey(TechDomain, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.URLField()
    
    # New Fields
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='Article')
    cost = models.CharField(max_length=10, choices=COST_TYPES, default='Free')

    def __str__(self):
        return f"{self.domain.name} - {self.title}"
    

class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.ForeignKey(TechDomain, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.result.name}"    