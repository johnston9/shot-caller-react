# Generated by Django 3.2.9 on 2023-03-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsheetsnew', '0011_auto_20221119_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='castcallnew',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
