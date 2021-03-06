# Generated by Django 3.2.9 on 2021-12-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='scene',
            new_name='scene10',
        ),
        migrations.AddField(
            model_name='day',
            name='location1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='location2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='location3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='location4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='location5',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene5',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene6',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene7',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene8',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='day',
            name='scene9',
            field=models.TextField(blank=True),
        ),
    ]
