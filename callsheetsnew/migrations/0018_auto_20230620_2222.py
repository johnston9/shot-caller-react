# Generated by Django 3.2.9 on 2023-06-20 22:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('callsheetsnew', '0017_auto_20230619_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extracrewinfo',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='extracrewinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extracrewinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='extracrewinfo',
            name='departments',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]