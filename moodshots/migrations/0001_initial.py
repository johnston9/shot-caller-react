# Generated by Django 3.2.9 on 2022-01-17 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Moodshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene', models.CharField(blank=True, max_length=255)),
                ('number', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('character', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('image1', models.ImageField(blank=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
