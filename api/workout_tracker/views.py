from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    UserSerializer, WorkoutLogSerializer,
    WorkoutSerializer, UserWorkoutTemplateSerializer,
    ExerciseSerializer, WorkoutTemplateSerializer,
    WorkoutTemplateExerciseSerializer,
)
from .models import (
    User, WorkoutLog, Workout, Exercise, 
    UserWorkoutTemplate,
    WorkoutTemplate, WorkoutTemplateExercise
)

class UserView(viewsets.ModekViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class WorkoutLogView(viewsets.ModekViewSet):
    serializer_class = WorkoutLogSerializer
    queryset = WorkoutLog.objects.all()

class WorkoutView(viewsets.ModekViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class ExerciseView(viewsets.ModekViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

class UserWorkoutTemplateView(viewsets.ModekViewSet):
    serializer_class = UserWorkoutTemplateSerializer
    queryset = UserWorkoutTemplate.objects.all()

class WorkoutTemplateView(viewsets.ModekViewSet):
    serializer_class = WorkoutTemplateSerializer
    queryset = WorkoutTemplate.objects.all()

class WorkoutTemplateExerciseView(viewsets.ModekViewSet):
    serializer_class = WorkoutTemplateExerciseSerializer
    queryset = WorkoutTemplateExercise.objects.all()
