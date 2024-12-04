from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class StudentView(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
