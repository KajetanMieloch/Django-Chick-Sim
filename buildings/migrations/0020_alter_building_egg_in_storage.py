# Generated by Django 4.2.5 on 2023-09-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0019_alter_building_egg_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='egg_in_storage',
            field=models.IntegerField(default=0),
        ),
    ]