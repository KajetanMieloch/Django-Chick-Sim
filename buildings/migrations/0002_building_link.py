# Generated by Django 4.2.5 on 2023-09-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='link',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
