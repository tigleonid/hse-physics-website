# Generated by Django 4.0.3 on 2022-06-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_announcement_options_alter_material_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialcontainer',
            name='files',
            field=models.ManyToManyField(to='main.file'),
        ),
    ]
