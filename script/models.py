"""
Model for the Script App
"""
from django.db import models


class Script(models.Model):
    """
    Script model
    """
    draft = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latest_changes = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    script = models.FileField(
        upload_to='images/', default='', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.draft}'
