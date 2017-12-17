"""Models for courses app."""
from django.db import models


# Create your models here.
class Course(models.Model):
    """Course Model to hold our various courses."""

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
