""" IndexShot1 Model """
from django.db import models


class IndexShot1(models.Model):
    """
    IndexShot1 model
    """
    number = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}'
