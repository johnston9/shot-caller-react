# Generated by Django 3.2.9 on 2024-08-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotlists', '0003_shotlist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shotlist',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
