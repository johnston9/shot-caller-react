# Generated by Django 3.2.9 on 2024-08-10 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_alter_day_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='date',
        ),
    ]
