""" Schedule Model """
from django.db import models


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
    character1_number = models.TextField(blank=True)
    character2 = models.TextField(blank=True)
    character2_costume = models.TextField(blank=True)
    character2_number = models.TextField(blank=True)
    character3 = models.TextField(blank=True)
    character3_costume = models.TextField(blank=True)
    character3_number = models.TextField(blank=True)
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
    other_characters_numbers = models.TextField(blank=True)
    background_artists = models.TextField(blank=True)
    background_artists_costumes = models.TextField(blank=True)
    new_content = models.TextField(blank=True)
    new_info = models.TextField(blank=True)

    class Meta:
        ordering = ['day_order_number']

    def __str__(self):
        return f'{self.number}'
