""" Shotlist Model """
from django.db import models
from scenes.models import Scene


class Shotlist(models.Model):
    """
    Related to Scene
    """
    scene_id = models.ForeignKey(Scene, on_delete=models.CASCADE)
    scene_number = models.CharField(max_length=255, blank=True)
    shot_number = models.IntegerField(blank=False)
    size = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    angle = models.TextField(blank=True)
    equipment = models.TextField(max_length=255, blank=True)
    movement = models.CharField(max_length=255, blank=True)
    fx = models.TextField(blank=True)
    focus_pulls = models.TextField(blank=True)
    lighting = models.TextField(blank=True)
    camera = models.TextField(blank=True)
    lens = models.TextField(blank=True)
    script_ref = models.TextField(blank=True)
    storyboard_refs = models.TextField(blank=True)
    audio = models.TextField(blank=True)
    framing = models.CharField(max_length=255, blank=True)
    int_ext = models.CharField(max_length=255, blank=True)
    frame_rate = models.CharField(max_length=255, blank=True)
    location = models.TextField(blank=True)
    actors = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    image = models.FileField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['scene_number', 'shot_number']

    def __str__(self):
        return f'{self.shot_number}'
