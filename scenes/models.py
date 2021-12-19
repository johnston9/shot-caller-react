"""
Model for Scenes App
"""
from django.db import models


class Scene(models.Model):
    """
    Scene model
    """
    EXT_INT_CHOICES = [
        ('ext', 'EXT.'),
        ('int', 'INT.'),
    ]
    DAY_NIGHT_CHOICES = [
        ('DAY', 'DAY'),
        ('NIGHT', 'NIGHT'),
    ]
    ACT_CHOICES = [
        ('one', 'One'),
        ('two-a', 'Two - First Half'),
        ('two-b', 'Two - Second Half'),
        ('three', 'Three'),
    ]
    number = models.IntegerField(blank=False)
    act = models.CharField(
        max_length=32, choices=ACT_CHOICES, default='one'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    int_ext = models.CharField(
        max_length=32, choices=EXT_INT_CHOICES, default='int'
    )
    day_night = models.CharField(
        max_length=32, choices=DAY_NIGHT_CHOICES, default='day'
    )
    time = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)
    characters = models.CharField(max_length=255, blank=True)
    action = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    shotlist = models.TextField(blank=True)
    storyboard = models.ImageField(
        upload_to='images/', default='', blank=True
    )
    info = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='', blank=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.location}'
