from dataclasses import fields
from rest_framework import serializers
from .models import (
    User, WorkoutLog, Workout, Exercise, 
    UserWorkoutTemplate,
    WorkoutTemplate, WorkoutTemplateExercise,
    ExerciseMusclesWorked
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password',
            'sex'
        )
        
class WorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = (
            'user_id',
            'workout_template_id',
            'workout_id',
            'date',
            'start_time',
            'end_time'
        )
       
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = (
            'workout_id',
            'exercise_id',
            'set_number',
            'weight',
            'reps'
        )

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            'exercise_id',
            'name',
            'description'
        )

class UserWorkoutTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutTemplate
        fields = (
            'workout_template_id',
            'user_id'
        )
       
class WorkoutTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTemplate
        fields = (
            'workout_template_id',
            'name',
            'description'
        )
        
class WorkoutTemplateExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTemplateExercise
        fields = (
            'workout_template_id',
            'exercise_id'
        )
        
class ExerciseMusclesWorkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseMusclesWorked
        fields = (
            'exercise_id',
            'muscle',
            'activation'
        )