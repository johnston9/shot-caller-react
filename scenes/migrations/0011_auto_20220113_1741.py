# Generated by Django 3.2.9 on 2022-01-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0010_scene_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='workspace_guide',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='scene',
            name='shooting_date',
            field=models.CharField(blank=True, default=3, max_length=255),
            preserve_default=False,
        ),
    ]