# Generated by Django 4.0.6 on 2022-07-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightlog',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
