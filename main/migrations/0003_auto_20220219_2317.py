# Generated by Django 3.1.3 on 2022-02-19 20:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20220219_2305'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Profile',
        ),
    ]
