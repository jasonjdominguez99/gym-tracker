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

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class WorkoutLogView(viewsets.ModelViewSet):
    serializer_class = WorkoutLogSerializer
    queryset = WorkoutLog.objects.all()

class WorkoutView(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class ExerciseView(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

class UserWorkoutTemplateView(viewsets.ModelViewSet):
    serializer_class = UserWorkoutTemplateSerializer
    queryset = UserWorkoutTemplate.objects.all()

class WorkoutTemplateView(viewsets.ModelViewSet):
    serializer_class = WorkoutTemplateSerializer
    queryset = WorkoutTemplate.objects.all()

class WorkoutTemplateExerciseView(viewsets.ModelViewSet):
    serializer_class = WorkoutTemplateExerciseSerializer
    queryset = WorkoutTemplateExercise.objects.all()
