from django.contrib import admin
from .models import (
    User, WorkoutLog, Workout, Exercise, 
    UserWorkoutTemplate,
    WorkoutTemplate, WorkoutTemplateExercise
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

class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'workout_template_id',
        'workout_id',
        'date',
        'start_time',
        'end_time'
    )

class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'workout_id',
        'exercise_id',
        'set_number',
        'weight',
        'reps'
    )

class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'exercise_id',
        'name',
        'description'
    )

class UserWorkoutTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'workout_template_id',
        'user_id'
    )

class WorkoutTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'workout_template_id',
        'name',
        'workout_exercises_id'
    )

class WorkoutTemplateExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'workout_exercises_id',
        'exercise_id'
    )

admin.site.register(User, UserAdmin)
admin.site.register(WorkoutLog, WorkoutLogAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(
    UserWorkoutTemplate, UserWorkoutTemplateAdmin
)
admin.site.register(WorkoutTemplate, WorkoutAdmin)
admin.site.register(
    WorkoutTemplateExercise,
    WorkoutTemplateExerciseAdmin
)
