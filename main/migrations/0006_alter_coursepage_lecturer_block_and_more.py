# Generated by Django 4.0.3 on 2022-05-30 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_file_file_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepage',
            name='lecturer_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_as_lect', to='main.block'),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='student_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages_as_st', to='main.block'),
        ),
        migrations.AlterField(
            model_name='material',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='main.block'),
        ),
    ]
