# Generated by Django 3.2.9 on 2022-03-10 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_auto_20220227_0026'),
        ('callsheets', '0003_auto_20220309_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Castcall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_number', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=255)),
                ('artist', models.CharField(blank=True, max_length=255)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('swf', models.CharField(blank=True, max_length=255)),
                ('pickup', models.CharField(blank=True, max_length=255)),
                ('call', models.TextField(blank=True)),
                ('hmw', models.TextField(blank=True)),
                ('on_set', models.TextField(blank=True)),
                ('inst', models.TextField(blank=True)),
                ('day_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.day')),
            ],
            options={
                'ordering': ['cast_number'],
            },
        ),
    ]
