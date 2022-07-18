# Generated by Django 4.0.6 on 2022-07-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exercisemusclesworked',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='exercisemusclesworked',
            name='activation',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Moderate'), ('L', 'Low')], default='M', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='exercisemusclesworked',
            unique_together={('exercise_id', 'muscle', 'activation')},
        ),
    ]