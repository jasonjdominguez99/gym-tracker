from django.contrib import admin
from .models import (
    User, WeightLog, WorkoutLog, 
    Workout, Exercise, UserWorkoutPlan,
    WorkoutPlan, WorkoutPlanExercise,
    ExerciseMusclesWorked
)

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "first_name",
        "last_name",
        "email",
        "password",
        "sex"
    )

class WeightLogAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'date',
        'weight',
        'units',
        'time',
        'notes'
    )

class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = (
        'workout_id',
        'name',
        'user_id',
        'date',
        'start_time',
        'end_time',
        'notes'
    )

class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'workout_id',
        'exercise_id',
        'set_number',
        'weight',
        'units',
        'reps',
        'notes'
    )

class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'exercise_id',
        'name',
        'description'
    )

class UserWorkoutPlanAdmin(admin.ModelAdmin):
    list_display = (
        'workout_plan_id',
        'user_id'
    )

class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = (
        'workout_plan_id',
        'name',
        'description'
    )

class WorkoutPlanExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'workout_plan_id',
        'exercise_id',
        'suggested_sets',
        'suggested_reps_min',
        'suggested_reps_max'
    )

class ExerciseMusclesWorkedAdmin(admin.ModelAdmin):
    flist_display = (
        'exercise_id',
        'muscle',
        'activation'
    )

admin.site.register(User, UserAdmin)
admin.site.register(WorkoutLog, WorkoutLogAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(
    UserWorkoutPlan, UserWorkoutPlanAdmin
)
admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(
    WorkoutPlanExercise,
    WorkoutPlanExerciseAdmin
)
admin.site.register(
    ExerciseMusclesWorked,
    ExerciseMusclesWorkedAdmin
)
