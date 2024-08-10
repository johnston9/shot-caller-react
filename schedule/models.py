""" Schedule Model """
from django.db import models
from scenes.models import Scene


class Day(models.Model):
    """
    Related to ScheduleScene
    """

    day = models.IntegerField(blank=False)
    date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['day']

    def __str__(self):
        return f'{self.day}'


class ScheduleScene(models.Model):
    """
    Related to Day
    """
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    scene_id = models.ForeignKey(Scene, on_delete=models.CASCADE)
    day = models.TextField(blank=True)
    day_order_number = models.IntegerField(blank=False)
    date = models.TextField(blank=True, default="")
    number = models.TextField(blank=True)
    act = models.TextField(blank=True)
    pages = models.CharField(max_length=255, blank=True)
    title = models.TextField(blank=True)
    start_time = models.TextField(blank=True)
    end_time = models.TextField(blank=True)
    int_ext = models.TextField(blank=True)
    day_night = models.TextField(blank=True)
    time = models.TextField(blank=True)
    action = models.TextField(blank=True)
    dramatic_day = models.TextField(blank=True)
    location = models.TextField(blank=True)
    location_detail = models.TextField(blank=True)
    filming_location = models.TextField(blank=True)
    location_address = models.TextField(blank=True)
    equip_set_props = models.TextField(blank=True)
    department_info = models.TextField(blank=True)
    next = models.TextField(blank=True)
    new_info = models.TextField(blank=True)

    class Meta:
        ordering = ['day_order_number']

    def __str__(self):
        return f'{self.number}'
