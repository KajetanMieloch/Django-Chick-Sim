# Generated by Django 4.2.5 on 2023-09-25 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0009_remove_building_income_per_click_per_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='cost_per_level',
        ),
        migrations.RemoveField(
            model_name='building',
            name='income_per_level',
        ),
    ]