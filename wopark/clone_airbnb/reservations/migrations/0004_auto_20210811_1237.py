# Generated by Django 2.2.5 on 2021-08-11 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20210811_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='geust',
            new_name='guest',
        ),
    ]