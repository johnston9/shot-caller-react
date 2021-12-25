""" Schedule Model """
from django.db import models
from django.contrib.auth.models import User
from scenes.models import Scene


class Day(models.Model):
    """
    Related to ScheduleScene
    """

    day = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    scene1 = models.TextField(blank=True)
    scene2 = models.TextField(blank=True)
    scene3 = models.TextField(blank=True)
    scene4 = models.TextField(blank=True)
    scene5 = models.TextField(blank=True)
    scene6 = models.TextField(blank=True)
    scene7 = models.TextField(blank=True)
    scene8  = models.TextField(blank=True)
    scene9 = models.TextField(blank=True)
    scene10 = models.TextField(blank=True)
    location1 = models.TextField(blank=True)
    location2 = models.TextField(blank=True)
    location3 = models.TextField(blank=True)
    location4 = models.TextField(blank=True)
    location5 = models.TextField(blank=True)

    class Meta:
        ordering = ['day']

    def __str__(self):
        return f'{self.day}'


# class ScheduleScene(models.Model):
#     """
#     Related to Day
#     """

#     day = models.CharField(max_length=255, blank=True)
#     date = models.DateField()
#     scene1_number = models.TextField(blank=True)
#     scene1_title = models.TextField(blank=True)
#     scene1_crewcall = models.TextField(blank=True)
#     scene1_start = models.TextField(blank=True)
#     scene1_script_location = models.TextField(blank=True)
#     scene1_filming_location = models.TextField(blank=True)
#     scene1_character1 = models.TextField(blank=True)
#     scene1_character1_costume = models.TextField(blank=True)
#     scene1_character1_calltime = models.TextField(blank=True)
#     scene1_character1_pickup = models.TextField(blank=True)
#     scene1_character2 = models.TextField(blank=True)
#     scene1_character2_costume = models.TextField(blank=True)
#     scene1_character2_calltime = models.TextField(blank=True)
#     scene1_character2_pickup = models.TextField(blank=True)
#     scene1_character3 = models.TextField(blank=True)
#     scene1_character3_costume = models.TextField(blank=True)
#     scene1_character4 = models.TextField(blank=True)
#     scene1_character4_costume = models.TextField(blank=True)
#     scene1_character5 = models.TextField(blank=True)
#     scene1_character5_costume = models.TextField(blank=True)
#     scene1_character6 = models.TextField(blank=True)
#     scene1_character6_costume = models.TextField(blank=True)
#     scene1_character7 = models.TextField(blank=True)
#     scene1_character7_costume = models.TextField(blank=True)
#     scene1_character8 = models.TextField(blank=True)
#     scene1_character8_costume = models.TextField(blank=True)
#     scene1_character9 = models.TextField(blank=True)
#     scene1_character9_costume = models.TextField(blank=True)
#     scene1_character10 = models.TextField(blank=True)
#     scene1_character10_costume = models.TextField(blank=True)
#     scene1_extra_characters = models.TextField(blank=True)
#     scene1_character_costumes = models.TextField(blank=True)
#     scene1_end = models.TextField(blank=True)
#     content = models.TextField(blank=True)

#     class Meta:
#         ordering = ['day']

#     def __str__(self):
#         return f'{self.day}'