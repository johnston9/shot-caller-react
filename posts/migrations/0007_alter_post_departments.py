# Generated by Django 3.2.9 on 2024-11-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_departments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='departments',
            field=models.CharField(choices=[('camera', 'Camera'), ('script', 'Script'), ('art', 'Art'), ('make-up', 'Hair/Makeup'), ('wardrobe', 'Wardrobe'), ('location', 'Location'), ('sound', 'Sound'), ('casting', 'Casting'), ('post', 'Post/VFX'), ('production', 'Production'), ('stunts', 'Stunts'), ('electric', 'Electric/Grip'), ('universal', 'Universal')], default='universal', max_length=32),
        ),
    ]