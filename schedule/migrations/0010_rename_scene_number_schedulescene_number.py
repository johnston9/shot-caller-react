# Generated by Django 3.2.9 on 2022-01-01 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_alter_schedulescene_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulescene',
            old_name='scene_number',
            new_name='number',
        ),
    ]
