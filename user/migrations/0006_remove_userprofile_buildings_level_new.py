# Generated by Django 4.2.5 on 2023-09-25 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_userprofile_buildings_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='buildings_level_new',
        ),
    ]
