# Generated by Django 3.2.9 on 2022-01-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_rename_scene_number_schedulescene_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulescene',
            name='location_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='schedulescene',
            name='date',
            field=models.TextField(blank=True, default=''),
        ),
    ]