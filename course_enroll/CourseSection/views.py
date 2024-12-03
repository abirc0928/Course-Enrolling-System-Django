from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from sections.models import *
from course.models import *
# from .serializers import *
# Create your views here.

class CourseSectionView(APIView):
    def get(self, request):
        course_section = CourseSection.objects.all()
        serializer = CourseSectionSerializer(course_section, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        