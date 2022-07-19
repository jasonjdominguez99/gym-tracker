from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    UserSerializer, WeightLogSerializer,
    WorkoutLogSerializer,
    WorkoutSerializer, UserWorkoutPlanSerializer,
    ExerciseSerializer, WorkoutPlanSerializer,
    WorkoutPlanExerciseSerializer,
    ExerciseMusclesWorkedSerializer
)
from .models import (
    User, WeightLog, WorkoutLog,
    Workout, Exercise, UserWorkoutPlan,
    WorkoutPlan, WorkoutPlanExercise,
    ExerciseMusclesWorked
)

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class WeightLogView(viewsets.ModelViewSet):
    serializer_class = WeightLogSerializer
    queryset = WeightLog.objects.all()

class WorkoutLogView(viewsets.ModelViewSet):
    serializer_class = WorkoutLogSerializer
    queryset = WorkoutLog.objects.all()

class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

class UserWorkoutPlanView(viewsets.ModelViewSet):
    serializer_class = UserWorkoutPlanSerializer
    queryset = UserWorkoutPlan.objects.all()

class WorkoutPlanView(viewsets.ModelViewSet):
    serializer_class = WorkoutPlanSerializer
    queryset = WorkoutPlan.objects.all()

class WorkoutPlanExerciseView(viewsets.ModelViewSet):
    serializer_class = WorkoutPlanExerciseSerializer
    queryset = WorkoutPlanExercise.objects.all()

class ExerciseMusclesWorkedView(viewsets.ModelViewSet):
    serializer_class = ExerciseMusclesWorkedSerializer
    queryset = ExerciseMusclesWorked.objects.all()
