# Generated by Django 4.2.5 on 2023-09-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_userprofile_egg_userprofile_egg_per_second_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinglevel',
            name='egg_in_storage',
            field=models.IntegerField(default=0),
        ),
    ]