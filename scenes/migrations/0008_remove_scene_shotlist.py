# Generated by Django 3.2.9 on 2021-12-29 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0007_auto_20211229_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene',
            name='shotlist',
        ),
    ]
