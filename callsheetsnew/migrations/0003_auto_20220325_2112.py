# Generated by Django 3.2.9 on 2022-03-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsheetsnew', '0002_auto_20220324_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='callsheetnew',
            name='director_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='director_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='director_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='director_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
