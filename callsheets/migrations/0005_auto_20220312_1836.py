# Generated by Django 3.2.9 on 2022-03-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsheets', '0004_castcall'),
    ]

    operations = [
        migrations.AddField(
            model_name='castcall',
            name='date',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='castcall',
            name='day',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]