# Generated by Django 3.1.3 on 2022-02-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='role',
            field=models.CharField(default='string', max_length=30),
            preserve_default=False,
        ),
    ]