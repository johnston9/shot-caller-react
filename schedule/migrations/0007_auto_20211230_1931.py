# Generated by Django 3.2.9 on 2021-12-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_schedulescene_new_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulescene',
            name='character11',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character11_calltime',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character11_costume',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character11_pickup',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character12',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character12_calltime',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character12_costume',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='character12_pickup',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='schedulescene',
            name='new_info',
            field=models.TextField(blank=True),
        ),
    ]
