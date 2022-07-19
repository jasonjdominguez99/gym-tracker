"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from workout_tracker.views import (
    UserView, WeightLogView,
    WorkoutLogView, WorkoutView,
    ExerciseView, UserWorkoutPlanView,
    WorkoutPlanView,
    WorkoutPlanExerciseView,
    ExerciseMusclesWorkedView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserView, 'user')
router.register(r'weight-log', WeightLogView, 'weight_log')
router.register(r'workout-log', WorkoutLogView, 'workout_log')
router.register(r'workouts', WorkoutView, 'workout')
router.register(r'exercises', ExerciseView, 'exercise')
router.register(
    r'user-workout-plans',
    UserWorkoutPlanView,
    'user_workout_plan'
)
router.register(
    r'workout-plans',
    WorkoutPlanView,
    'workout_plan'
)
router.register(
    r'workout-plan-exercises',
    WorkoutPlanExerciseView,
    'workout_plan_exercise'
)
router.register(
    r'exercises-muscles-worked',
    ExerciseMusclesWorkedView,
    'exercise_muscles_worked'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
