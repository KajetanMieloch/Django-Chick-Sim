# Generated by Django 4.2.5 on 2023-09-24 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='department_images')),
            ],
            options={
                'verbose_name': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Chicken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_bought', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='chicken_images')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.department')),
            ],
            options={
                'verbose_name': 'Chicken',
            },
        ),
    ]
