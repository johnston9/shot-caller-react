""" IndexCard Model """
from django.db import models


class IndexCard(models.Model):
    """
    IndexCard model
    """
    number = models.CharField(max_length=255, blank=True)
    story = models.TextField(blank=True)
    style = models.TextField(blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}'
