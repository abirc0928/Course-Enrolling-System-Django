from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class StudentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
