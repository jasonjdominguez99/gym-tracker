from dataclasses import fields
from rest_framework import serializers
from .models import (
    User, WeightLog, WorkoutLog, Workout,
    Exercise, UserWorkoutPlan,
    WorkoutPlan, WorkoutPlanExercise,
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

class WeightLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightLog
        fields = (
            'user_id',
            'date',
            'weight',
            'units',
            'time',
            'notes'
        )

class WorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = (
            'workout_id',
            'name',
            'user_id',
            'date',
            'start_time',
            'end_time',
            'notes'
        )
       
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = (
            'workout_id',
            'exercise_id',
            'set_number',
            'weight',
            'units',
            'reps',
            'notes'
        )

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            'exercise_id',
            'name',
            'description'
        )

class UserWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutPlan
        fields = (
            'workout_plan_id',
            'user_id'
        )
       
class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = (
            'workout_plan_id',
            'name',
            'description'
        )
        
class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanExercise
        fields = (
            'workout_plan_id',
            'exercise_id',
            'suggested_sets',
            'suggested_reps_min',
            'suggested_reps_max'
        )
        
class ExerciseMusclesWorkedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseMusclesWorked
        fields = (
            'exercise_id',
            'muscle',
            'activation'
        )
