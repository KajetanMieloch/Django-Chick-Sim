# Generated by Django 4.2.5 on 2023-09-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0013_alter_building_cost_alter_building_cost_in_egg_and_more'),
        ('user', '0006_remove_userprofile_buildings_level_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='buildings_level',
            field=models.ManyToManyField(related_name='user_profile_levels_new', through='user.BuildingLevel', to='buildings.building'),
        ),
    ]
