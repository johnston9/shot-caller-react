# Generated by Django 3.2.9 on 2024-08-10 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0020_alter_day_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
