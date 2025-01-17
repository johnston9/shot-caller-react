# Generated by Django 3.2.9 on 2024-10-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_alter_department_departments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='departments',
            field=models.CharField(choices=[('camera', 'Camera'), ('script', 'Script'), ('art', 'Art'), ('make-up', 'Hair/Makeup'), ('wardrobe', 'Wardrobe'), ('location', 'Location'), ('sound', 'Sound'), ('casting', 'Casting'), ('post', 'Post/VFX'), ('production', 'Production'), ('stunts', 'Stunts'), ('electric', 'Electric/Grip'), ('latest', 'Latest')], default='camera', max_length=32),
        ),
    ]
