from django.db import models
import uuid

class User(models.Model):
    sexes = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Non-binary')
    ]

    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.EmailField()
    password = models.CharField(max_length=127)
    sex = models.CharField(max_length=1, choices=sexes, blank=True)

    def __str__(self):
        return self.first_name + self.last_name

class WorkoutLog(models.Model):
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    workout_template_id = models.ForeignKey(
        'WorkoutTemplate',
        on_delete=models.CASCADE,
    )
    workout_id = models.ForeignKey(
        'Workout',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)

    class Meta:
        unique_together = [
            'user_id', 
            'workout_template_id', 
            'workout_id'
        ]

    def __str__(self):
        return self(self.date)

class Workout(models.Model):
    workout_id = models.AutoField(
        primary_key=True, editable=False
    )
    exercise_id = models.ForeignKey(
        'Exercise',
        on_delete=models.CASCADE
    )
    set_number = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.workout_id)

class Exercise(models.Model):
    exercise_id = models.AutoField(
        primary_key=True, editable=False
    )
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserWorkoutTemplate(models.Model):
    workout_template_id = models.ForeignKey(
        'WorkoutTemplate',
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            "User: " + str(self.user_id)
            + " Workout template: "
            + str(self.workout_template_id)
        )

class WorkoutTemplate(models.Model):
    workout_template_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=127)
    workout_exercises_id = models.ForeignKey(
        'WorkoutTemplateExercise',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class WorkoutTemplateExercise(models.Model):
    workout_exercises_id = models.AutoField(
        primary_key=True, editable=False
    )
    exercise_id = models.ForeignKey(
        'Exercise',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.workout_exercises_id)
