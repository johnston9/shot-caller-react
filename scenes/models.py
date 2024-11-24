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
    location_detail = models.CharField(max_length=255, blank=True)
    dramatic_day = models.CharField(max_length=255, blank=True)
    department_info = models.TextField(blank=True)
    equip_set_props = models.TextField(blank=True)
    int_ext = models.CharField(
        max_length=32, choices=EXT_INT_CHOICES, blank=True
    )
    day_night = models.CharField(
        max_length=32, choices=DAY_NIGHT_CHOICES, blank=True
    )
    pages = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    filming_location = models.CharField(max_length=255, blank=True)
    shooting_date = models.CharField(max_length=255, blank=True, default="")
    action = models.CharField(max_length=255, blank=True)
    workspace_guide = models.TextField(blank=True)
    storyboard_url = models.CharField(max_length=255, blank=True)
    storyboard = models.FileField(
        upload_to='images/', default='', blank=True
    )
    script = models.FileField(
        upload_to='images/', default='', blank=True
    )

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.location}'


class SceneCharacterAdd(models.Model):
    """
    SceneCharacterAdd Model
    """

    scene_id = models.ForeignKey(Scene, on_delete=models.CASCADE)
    cast_number = models.IntegerField(blank=False)
    role = models.CharField(max_length=255, blank=True)
    costume = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['cast_number']

    def __str__(self):
        return f'{self.role}'


class SceneBGAdd(models.Model):
    """
    SceneBGAdd Model
    """

    scene_id = models.ForeignKey(Scene, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)
    costume = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['role']

    def __str__(self):
        return f'{self.role}'
