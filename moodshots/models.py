""" Moodshots Model """
from django.db import models
from django.contrib.auth.models import User
from scenes.models import Scene


class Moodshot(models.Model):
    """
    Moodshot model, related to 'owner', i.e. a User instance.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    scene = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    character = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    image1 = models.ImageField(
        upload_to='images/', blank=True
    )
    image2 = models.ImageField(
        upload_to='images/', blank=True
    )
    image3 = models.ImageField(
        upload_to='images/', blank=True
    )
    image4 = models.ImageField(
        upload_to='images/', blank=True
    )
    image5 = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.number} {self.title}'
