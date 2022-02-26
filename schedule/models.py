""" Schedule Model """
from django.db import models
# from scenes.models import Scene


class Day(models.Model):
    """
    Related to ScheduleScene
    """

    day = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)
    crewcall = models.TextField(blank=True)
    scene1 = models.TextField(blank=True)
    scene2 = models.TextField(blank=True)
    scene3 = models.TextField(blank=True)
    scene4 = models.TextField(blank=True)
    scene5 = models.TextField(blank=True)
    scene6 = models.TextField(blank=True)
    scene7 = models.TextField(blank=True)
    scene8 = models.TextField(blank=True)
    scene9 = models.TextField(blank=True)
    scene10 = models.TextField(blank=True)
    scene11 = models.TextField(blank=True)
    scene12 = models.TextField(blank=True)
    xtra_scenes = models.TextField(blank=True)
    location1 = models.TextField(blank=True)

    class Meta:
        ordering = ['day']

    def __str__(self):
        return f'{self.day}'


class ScheduleScene(models.Model):
    """
    Related to Day
    """
    day_id = models.ForeignKey(Day, on_delete=models.CASCADE)
    day = models.TextField(blank=True)
    day_order_number = models.CharField(max_length=255, blank=True)
    date = models.TextField(blank=True, default="")
    number = models.TextField(blank=True)
    act = models.TextField(blank=True)
    pages = models.CharField(max_length=255, blank=True)
    title = models.TextField(blank=True)
    start_time = models.TextField(blank=True)
    end_time = models.TextField(blank=True)
    content = models.TextField(blank=True)
    location = models.TextField(blank=True)
    filming_location = models.TextField(blank=True)
    location_address = models.TextField(blank=True)
    int_ext = models.TextField(blank=True)
    day_night = models.TextField(blank=True)
    time = models.TextField(blank=True)
    action = models.TextField(blank=True)
    info = models.TextField(blank=True)
    character1 = models.TextField(blank=True)
    character1_costume = models.TextField(blank=True)
    character1_calltime = models.TextField(blank=True, default='')
    character1_pickup = models.TextField(blank=True, default='')
    character2 = models.TextField(blank=True)
    character2_costume = models.TextField(blank=True)
    character2_calltime = models.TextField(blank=True, default='')
    character2_pickup = models.TextField(blank=True, default='')
    character3 = models.TextField(blank=True)
    character3_costume = models.TextField(blank=True)
    character3_calltime = models.TextField(blank=True, default='')
    character3_pickup = models.TextField(blank=True, default='')
    character4 = models.TextField(blank=True)
    character4_costume = models.TextField(blank=True)
    character4_calltime = models.TextField(blank=True, default='')
    character4_pickup = models.TextField(blank=True, default='')
    character5 = models.TextField(blank=True)
    character5_costume = models.TextField(blank=True)
    character5_calltime = models.TextField(blank=True, default='')
    character5_pickup = models.TextField(blank=True, default='')
    character6 = models.TextField(blank=True)
    character6_costume = models.TextField(blank=True)
    character6_calltime = models.TextField(blank=True, default='')
    character6_pickup = models.TextField(blank=True, default='')
    character7 = models.TextField(blank=True)
    character7_costume = models.TextField(blank=True)
    character7_calltime = models.TextField(blank=True, default='')
    character7_pickup = models.TextField(blank=True, default='')
    character8 = models.TextField(blank=True)
    character8_costume = models.TextField(blank=True)
    character8_calltime = models.TextField(blank=True, default='')
    character8_pickup = models.TextField(blank=True, default='')
    character9 = models.TextField(blank=True)
    character9_costume = models.TextField(blank=True)
    character9_calltime = models.TextField(blank=True, default='')
    character9_pickup = models.TextField(blank=True, default='')
    character10 = models.TextField(blank=True)
    character10_costume = models.TextField(blank=True)
    character10_calltime = models.TextField(blank=True, default='')
    character10_pickup = models.TextField(blank=True, default='')
    character11 = models.TextField(blank=True)
    character11_costume = models.TextField(blank=True)
    character11_calltime = models.TextField(blank=True, default='')
    character11_pickup = models.TextField(blank=True, default='')
    character12 = models.TextField(blank=True)
    character12_costume = models.TextField(blank=True)
    character12_calltime = models.TextField(blank=True, default='')
    character12_pickup = models.TextField(blank=True, default='')
    other_characters = models.TextField(blank=True)
    other_characters_costumes = models.TextField(blank=True)
    other_characters_calltimes = models.TextField(blank=True)
    other_characters_pickups = models.TextField(blank=True)
    background_artists = models.TextField(blank=True)
    background_artists_costumes = models.TextField(blank=True)
    background_artists_calltimes = models.TextField(blank=True)
    background_artists_pickups = models.TextField(blank=True)
    new_content = models.TextField(blank=True)
    new_info = models.TextField(blank=True)

    class Meta:
        ordering = ['day_order_number']

    def __str__(self):
        return f'{self.number}'
