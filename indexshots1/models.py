""" IndexShot1 Models """
from django.db import models


class Series(models.Model):
    """
    Related to IndexShot
    """

    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class IndexShot(models.Model):
    """
    IndexShot model
    """
    series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}'
