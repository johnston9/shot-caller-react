# Generated by Django 3.2.9 on 2021-11-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_nhsuxh', upload_to='images/'),
        ),
    ]
