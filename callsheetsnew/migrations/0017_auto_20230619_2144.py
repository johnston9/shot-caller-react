# Generated by Django 3.2.9 on 2023-06-19 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsheetsnew', '0016_extracrewinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callsheetnew',
            old_name='xtra_camera_pos_10_calltime',
            new_name='add_pos_11_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='all_other_add_positions_calltimes',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_1_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_2_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_3_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_4_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_5_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_6_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_7_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_8_calltime',
        ),
        migrations.RemoveField(
            model_name='callsheetnew',
            name='xtra_camera_pos_9_calltime',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='all_other_add_positions',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_10_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_10_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_10_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_10_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_1_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_1_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_1_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_1_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_2_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_2_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_2_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_2_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_3_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_3_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_3_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_3_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_4_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_4_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_4_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_4_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_5_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_5_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_5_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_5_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_6_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_6_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_6_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_6_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_7_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_7_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_7_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_7_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_8_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_8_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_8_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_8_phone',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_9_email',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_9_job',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_9_name',
        ),
        migrations.RemoveField(
            model_name='crewinfonew',
            name='xtra_camera_pos_9_phone',
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_12_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_13_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_14_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_15_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_16_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_17_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_18_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_19_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_20_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_11_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_11_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_11_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_11_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_12_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_12_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_12_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_12_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_13_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_13_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_13_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_13_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_14_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_14_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_14_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_14_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_15_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_15_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_15_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_15_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_16_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_16_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_16_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_16_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_17_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_17_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_17_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_17_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_18_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_18_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_18_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_18_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_19_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_19_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_19_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_19_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_20_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_20_job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_20_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='crewinfonew',
            name='add_pos_20_phone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
