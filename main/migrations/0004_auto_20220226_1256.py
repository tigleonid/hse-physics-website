# Generated by Django 3.1.3 on 2022-02-26 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220226_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
