# Generated by Django 3.2.9 on 2024-08-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenes', '0022_auto_20221204_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='storyboard_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='scene',
            name='storyboard',
            field=models.FileField(blank=True, default='', upload_to='images/'),
        ),
    ]
