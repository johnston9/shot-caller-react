# Generated by Django 3.2.9 on 2021-11-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0002_auto_20211113_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='chatacters',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
