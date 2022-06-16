""" IndexCard Model """
from django.db import models


class IndexCard(models.Model):
    """
    IndexCard model
    """
    number = models.IntegerField(blank=False)
    story = models.TextField(blank=True)
    style = models.TextField(blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}'
