from django.db import models
from django.contrib.auth.models import User
from scenes.models import Scene


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Related to scene.
    """
    department_choices = [
        ('camera', 'Camera'), ('script', 'Script'), ('art', 'Art'),
        ('make-up', 'Hair/Make-up'), ('wardrobe', 'Wardrobe'),
        ('location', 'Location'), ('sound', 'Sound'),
        ('casting', 'Casting'), ('post', 'Post/VSF'),
        ('production', 'Production'), ('stunts', 'Stunts'),
        ('electric', 'Electric/Grip'),
     ]

    category_choices = [
        ('requirements', 'Requirements'), ('workspace', 'Workspace'),
        ('finals', 'Finals'), ('shooting', 'Shooting'), ('info', 'Info'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, default='1')
    departments = models.CharField(
        max_length=32, choices=department_choices, default='camera'
    )
    category = models.CharField(
        max_length=32, choices=category_choices, default='info'
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
        return f'{self.scene} {self.title}'
