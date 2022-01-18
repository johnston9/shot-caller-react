""" Locations Model """
from django.db import models


class Location(models.Model):
    """
    Location model.
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    filming_address_primary = models.TextField(blank=True)
    filming_address2 = models.TextField(blank=True)
    filming_address3 = models.TextField(blank=True)
    image1_description = models.TextField(blank=True)
    image1 = models.ImageField(
        upload_to='images/', blank=True
    )
    image2_description = models.TextField(blank=True)
    image2 = models.ImageField(
        upload_to='images/', blank=True
    )
    image3_description = models.TextField(blank=True)
    image3 = models.ImageField(
        upload_to='images/', blank=True
    )
    image4_description = models.TextField(blank=True)
    image4 = models.ImageField(
        upload_to='images/', blank=True
    )
    image5_description = models.TextField(blank=True)
    image5 = models.ImageField(
        upload_to='images/', blank=True
    )
    image6_description = models.TextField(blank=True)
    image6 = models.ImageField(
        upload_to='images/', blank=True
    )
    image7_description = models.TextField(blank=True)
    image7 = models.ImageField(
        upload_to='images/', blank=True
    )
    image8_description = models.TextField(blank=True)
    image8 = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
