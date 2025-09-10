from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('agent', 'Agent'),
        ('user', 'User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)

    # New agent-specific fields:
    specialization = models.CharField(max_length=100, blank=True, null=True)
    properties_sold = models.PositiveIntegerField(default=0)
    years_experience = models.PositiveIntegerField(default=0)
    client_satisfaction = models.FloatField(default=0.0)  # percentage (e.g., 97.5)
    description = models.TextField(blank=True, null=True)
    property_types = models.CharField(max_length=200, blank=True, null=True, help_text="Comma-separated list of property types")
    rating = models.FloatField(default=0.0)  # e.g., 4.5 stars

    def __str__(self):
        return f"{self.user.username} - {self.role}"
