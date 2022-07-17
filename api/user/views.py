from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User

# Create your views here.
class UserView(viewsets.ModekViewSet):
    serializer_class - UserSerializer
    queryset = User.objects.all()
