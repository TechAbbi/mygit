# Generated by Django 5.0 on 2023-12-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_item_item_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='name',
        ),
    ]