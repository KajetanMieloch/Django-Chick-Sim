# Generated by Django 4.2.5 on 2023-09-27 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_rename_shopping_items_shopping_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping_item',
            new_name='Shoppingitem',
        ),
    ]