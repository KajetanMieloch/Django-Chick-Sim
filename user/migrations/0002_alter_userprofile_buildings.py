# Generated by Django 4.2.5 on 2023-09-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_alter_building_options_remove_building_link_and_more'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='buildings',
            field=models.ManyToManyField(to='buildings.building'),
        ),
    ]