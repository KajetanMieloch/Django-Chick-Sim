# Generated by Django 4.2.5 on 2023-09-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_userprofile_int_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='int_array',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
