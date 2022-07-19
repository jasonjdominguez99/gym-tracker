from django.db import models
import uuid

weight_units = [
    ('kg', 'kg'),
    ('lbs', 'lbs')
]

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
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=127)
    sex = models.CharField(max_length=1, choices=sexes, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class WeightLog(models.Model):
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    units = models.CharField(
        max_length=3, choices=weight_units
    )
    time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = [
            'user_id',
            'date',
            'time'
        ]

    def __str__(self):
        return f"User: {self.user_id} {self.date} \
                 {self.time}"

class WorkoutLog(models.Model):
    workout_id = models.AutoField(
        primary_key=True, editable=False
    )
    name = models.CharField(max_length=127)
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user_id}: {self.date} {self.name}"

class Workout(models.Model):
    workout_id = models.ForeignKey(
        'WorkoutLog',
        on_delete=models.CASCADE
    )
    exercise_id = models.ForeignKey(
        'Exercise',
        on_delete=models.CASCADE
    )
    set_number = models.PositiveSmallIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    units = models.CharField(max_length=3, choices=weight_units)
    reps = models.PositiveSmallIntegerField()
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = [
            'workout_id',
            'exercise_id',
            'set_number'
        ]

    def __str__(self):
        return f"{self.workout_id}: {self.exercise_id} \
                 Set {self.set_number}"

class Exercise(models.Model):
    exercise_id = models.AutoField(
        primary_key=True, editable=False
    )
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class UserWorkoutPlan(models.Model):
    workout_plan_id = models.ForeignKey(
        'WorkoutPlan',
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"User: {self.user_id} \
                 Workout plan: {self.workout_plan_id}"

class WorkoutPlan(models.Model):
    workout_plan_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class WorkoutPlanExercise(models.Model):
    workout_plan_id = models.ForeignKey(
        'WorkoutPlan',
        on_delete=models.CASCADE
    )
    exercise_id = models.ForeignKey(
        'Exercise',
        on_delete=models.CASCADE
    )
    suggested_sets = models.PositiveSmallIntegerField()
    suggested_reps_min = models.PositiveSmallIntegerField()
    suggested_reps_max = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [
            'workout_plan_id',
            'exercise_id'
        ]

    def __str__(self):
        return f"Workout plan: {self.workout_plan_id} \
                 Exercise: {self.exercise_id}"

class ExerciseMusclesWorked(models.Model):
    muscles = [
        'Deltoid', 'Anterior Deltoid', 'Lateral Deltoid',
        'Posterior Deltoid', 'Biceps', 'Triceps',
        'Gluteus Maximus', 'Gluteus Medius', 'Quadriceps',
        'Hamstrings', 'Tibialis Anterior', 'Gastrocnemius',
        'Soleus', 'Pectoralis Major', 'Rectus Abdominis',
        'External Oblique', 'Trapezius', 'Rhomboids',
        'Latissimus Dorsi', 'Erector Spinae'
    ]
    muscles = [(muscle, muscle) for muscle in muscles]

    activations = [
        ('H', 'High'),
        ('M', 'Moderate'),
        ('L', 'Low')
    ]

    exercise_id = models.ForeignKey(
        'Exercise',
        on_delete=models.CASCADE
    )
    muscle = models.CharField(max_length=127, choices=muscles)
    activation = models.CharField(max_length=10, choices=activations, default='M')

    class Meta:
        unique_together = [
            'exercise_id',
            'muscle'
        ]

    def __str__(self):
        return f"Exercise: {self.exercise_id} \
                 Muscle worked: {self.muscle}"
