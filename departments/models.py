""" Departments Model """
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    """
    Department model, related to 'owner', i.e. a User instance.
    """
    department_choices = [
        ('camera', 'Camera'), ('script', 'Script'), ('art', 'Art'),
        ('make-up', 'Hair/Make-up'), ('wardrobe', 'Wardrobe'),
        ('location', 'Location'), ('sound', 'Sound'),
        ('casting', 'Casting'), ('post', 'Post/VSF'),
        ('production', 'Production'), ('stunts', 'Stunts'),
        ('electric', 'Electric/Grip'),
     ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    departments = models.CharField(
        max_length=32, choices=department_choices, default='camera'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
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
        return f'{self.owner} {self.title}'
