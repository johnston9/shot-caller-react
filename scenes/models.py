"""
Model for the Scenes App
"""
from django.db import models


class Scene(models.Model):
    """
    Scene model
    """
    EXT_INT_CHOICES = [
        ('ext', 'EXT.'),
        ('int', 'INT.'),
    ]
    DAY_NIGHT_CHOICES = [
        ('DAY', 'DAY'),
        ('NIGHT', 'NIGHT'),
    ]
    ACT_CHOICES = [
        ('one', 'One'),
        ('two-a', 'Two - First Half'),
        ('two-b', 'Two - Second Half'),
        ('three', 'Three'),
    ]
    number = models.IntegerField(blank=False)
    title = models.CharField(max_length=255, blank=True)
    act = models.CharField(
        max_length=32, choices=ACT_CHOICES, default='one', blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True)
    dramatic_day = models.CharField(max_length=255, blank=True)
    department_info = models.TextField(blank=True)
    equip_set_props = models.TextField(blank=True)
    int_ext = models.CharField(
        max_length=32, choices=EXT_INT_CHOICES, default='int', blank=True
    )
    day_night = models.CharField(
        max_length=32, choices=DAY_NIGHT_CHOICES, default='day', blank=True
    )
    pages = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    filming_location = models.CharField(max_length=255, blank=True)
    shooting_date = models.CharField(max_length=255, blank=True, default="")
    action = models.CharField(max_length=255, blank=True)
    character1 = models.TextField(blank=True)
    character1_costume = models.TextField(blank=True)
    character2 = models.TextField(blank=True)
    character2_costume = models.TextField(blank=True)
    character3 = models.TextField(blank=True)
    character3_costume = models.TextField(blank=True)
    character4 = models.TextField(blank=True)
    character4_costume = models.TextField(blank=True)
    character5 = models.TextField(blank=True)
    character5_costume = models.TextField(blank=True)
    character6 = models.TextField(blank=True)
    character6_costume = models.TextField(blank=True)
    character7 = models.TextField(blank=True)
    character7_costume = models.TextField(blank=True)
    character8 = models.TextField(blank=True)
    character8_costume = models.TextField(blank=True)
    character9 = models.TextField(blank=True)
    character9_costume = models.TextField(blank=True)
    character10 = models.TextField(blank=True)
    character10_costume = models.TextField(blank=True)
    character11 = models.TextField(blank=True)
    character11_costume = models.TextField(blank=True)
    character12 = models.TextField(blank=True)
    character12_costume = models.TextField(blank=True)
    character1_number = models.TextField(blank=True)
    character2_number = models.TextField(blank=True)
    character3_number = models.TextField(blank=True)
    character4_number = models.TextField(blank=True)
    character5_number = models.TextField(blank=True)
    character6_number = models.TextField(blank=True)
    character7_number = models.TextField(blank=True)
    character8_number = models.TextField(blank=True)
    character9_number = models.TextField(blank=True)
    character10_number = models.TextField(blank=True)
    character11_number = models.TextField(blank=True)
    character12_number = models.TextField(blank=True)
    other_characters = models.TextField(blank=True)
    other_characters_costumes = models.TextField(blank=True)
    background_artists = models.TextField(blank=True)
    background_artists_costumes = models.TextField(blank=True)
    workspace_guide = models.TextField(blank=True)
    storyboard = models.ImageField(
        upload_to='images/', default='', blank=True
    )
    script = models.FileField(
        upload_to='images/', default='', blank=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.location}'
