# Generated by Django 4.2.5 on 2023-09-24 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chicken',
            name='is_bought',
        ),
    ]
