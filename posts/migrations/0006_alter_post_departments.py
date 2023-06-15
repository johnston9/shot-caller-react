# Generated by Django 3.2.9 on 2023-06-15 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220113_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='departments',
            field=models.CharField(choices=[('camera', 'Camera'), ('script', 'Script'), ('art', 'Art'), ('make-up', 'Hair/Makeup'), ('wardrobe', 'Wardrobe'), ('location', 'Location'), ('sound', 'Sound'), ('casting', 'Casting'), ('post', 'Post/FXS'), ('production', 'Production'), ('stunts', 'Stunts'), ('electric', 'Electric/Grip'), ('universal', 'Universal')], default='universal', max_length=32),
        ),
    ]
