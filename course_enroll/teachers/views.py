from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from .models import Teachers
# Create your views here.

class TeacherView(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer