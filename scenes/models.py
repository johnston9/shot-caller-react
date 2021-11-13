from django.db import models


class Scene(models.Model):
    """
    Scene model
    """
    EXT_INT_CHOICES = [
        ('ext', 'EXT.'),
        ('int', 'INT.'),
    ]
    number = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    int_ext = models.CharField(
        max_length=32, choices=EXT_INT_CHOICES, default='int'
    )
    time = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)
    chatacters = models.CharField(max_length=255, blank=True)
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
