# Generated by Django 3.2.9 on 2022-03-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsheetsnew', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crewinfonew',
            old_name='a0dd_pos_9_job',
            new_name='add_pos_9_job',
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ad_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ad_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ad_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ad_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ad_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_10_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_6_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_7_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_8_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='add_pos_9_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='art_assistant_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='art_director_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ass_costume_designer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='ass_prop_master_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='best_boy_electric_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='best_boy_grip_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='boom_operator_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='camera_ass_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='camera_ass_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='camera_operator_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='camera_pa_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='car1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='car2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='car3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='casting_director_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='catering_co_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='catering_co_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='catering_co_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='costume_designer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='craft_service_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='crafty_ass_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='dit_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='dolly_grip_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='dop_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='dresser_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='editor_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='electric_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='electric_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='extras_casting_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='fx_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='gaffer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='head_driver_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='key_hairmakeup_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='key_hairstylist_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='keygrip_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='lead_man_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='legal_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='location_ass_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='location_ass_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='location_ass_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='location_ass_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='location_mngr_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='location_security_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='makeup_artist_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='makeup_artist_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='makeup_artist_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='makeup_artist_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='makeup_artist_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_camera_pos_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_camera_pos_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_camera_pos_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_production_pos_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_production_pos_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_production_pos_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_production_pos_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='oth_production_pos_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='pro_assistant_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='pro_assistant_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='pro_assistant_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='pro_assistant_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='pro_assistant_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='pro_coordinator_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='producer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='production_pa_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='prop_buyer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='prop_master_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='script_supervisor_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='set_decorator_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='set_dresser_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='set_medic_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='sfx_makeup_assistant_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='sfx_makeup_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='sound_assistant_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='sound_assistant_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='sound_mixer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='steadicam_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='stunt_coordinator_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='stunts_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='stunts_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='stunts_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='stunts_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='stunts_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='swing_ge1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='swing_ge2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='swing_ge3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='swing_ge4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='swing_ge5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='transport_captain_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='transport_manager_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='transport_manager_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='travel_coordinator_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='truck1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='truck2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='truck3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='upm_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='wardrobe_assistant_1_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='wardrobe_assistant_2_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='wardrobe_assistant_3_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='wardrobe_assistant_4_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='wardrobe_assistant_5_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='callsheetnew',
            name='writer_calltime',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]