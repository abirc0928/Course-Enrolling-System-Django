from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from student_course.models import StudentCourse
# Create your views here.

class StudentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
class StudentCourseView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        student = Students.objects.get(id=pk)
        serializer = StudentCourseSerializer(student)
        return Response(serializer.data)