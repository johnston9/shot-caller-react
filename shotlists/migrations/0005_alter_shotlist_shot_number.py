# Generated by Django 3.2.9 on 2024-08-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shotlists', '0004_alter_shotlist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shotlist',
            name='shot_number',
            field=models.IntegerField(),
        ),
    ]
