""" Characters Model """
from django.db import models


class Character(models.Model):
    """
    Character model
    """
    number = models.CharField(max_length=255, blank=False)
    role = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    actor = models.CharField(max_length=255, blank=True)
    pickup_address = models.TextField(blank=True)
    pickup_address_2 = models.TextField(blank=True)
    make_up_time = models.CharField(max_length=255, blank=True)
    commute_time = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    agent = models.CharField(max_length=255, blank=True)
    diet = models.CharField(max_length=255, blank=True)
    requirements = models.CharField(max_length=255, blank=True)
    costume1 = models.TextField(blank=True)
    costume1_image = models.ImageField(
        upload_to='images/', blank=True
    )
    costume2 = models.TextField(blank=True)
    costume2_image = models.ImageField(
        upload_to='images/', blank=True
    )
    costume3 = models.TextField(blank=True)
    costume3_image = models.ImageField(
        upload_to='images/', blank=True
    )
    costume4 = models.TextField(blank=True)
    costume4_image = models.ImageField(
        upload_to='images/', blank=True
    )
    costume5 = models.TextField(blank=True)
    costume5_image = models.ImageField(
        upload_to='images/', blank=True
    )
    costume6 = models.TextField(blank=True)
    costume6_image = models.ImageField(
        upload_to='images/', blank=True
    )
    costume7 = models.TextField(blank=True)
    costume7_image = models.ImageField(
        upload_to='images/', blank=True
    )
    makeup = models.TextField(blank=True)
    makeup_image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['role']

    def __str__(self):
        return f'{self.role}'
