# Generated by Django 3.2.9 on 2021-12-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0008_remove_scene_shotlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='character11',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='character11_costume',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='character12',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='character12_costume',
            field=models.TextField(blank=True),
        ),
    ]
