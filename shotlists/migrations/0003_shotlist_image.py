# Generated by Django 3.2.9 on 2022-01-08 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotlists', '0002_shotlist_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='shotlist',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
