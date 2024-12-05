from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from .models import Teachers
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TeacherView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer