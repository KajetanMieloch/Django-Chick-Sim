# Generated by Django 4.2.5 on 2023-09-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20230925_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildinglevel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
