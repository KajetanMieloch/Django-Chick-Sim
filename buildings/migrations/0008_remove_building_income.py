# Generated by Django 4.2.5 on 2023-09-25 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0007_remove_building_cost_in_egg_building_egg_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='income',
        ),
    ]
