
from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *
from sections.models import *
from course.models import *

# from .serializers import *
# Create your views here.

class CourseSectionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        course_section = CourseSection.objects.all()
        serializer = CourseSectionSerializer(course_section, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSectionSerializer(data=request.data)
        serializer.context['request_method'] = request.method
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   

class CourseSectionViewDetails(APIView):
     permission_classes = [IsAuthenticated]
     def put(self, request, pk):
        print("updatate")
        try:
            course_section = CourseSection.objects.get(pk=pk)
        except CourseSection.DoesNotExist:
            raise NotFound(detail="CourseSection not found.")
        print(request.data)
        print(course_section)

        serializer = CourseSectionSerializer(course_section, data=request.data, partial=True)
        serializer.context['request_method'] = request.method
        if serializer.is_valid():
            serializer.save()  # This will update the CourseSection with the new data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     def delete(self, request, pk):
        try:
            course_section = CourseSection.objects.get(pk=pk)
        except CourseSection.DoesNotExist:    
            raise NotFound(detail="CourseSection not found.")
        course_section.delete()
        course_section = CourseSection.objects.all()
        serializer = CourseSectionSerializer(course_section, many=True)
        return Response(serializer.data)
      

     def get(self, request, pk):
        try:    
            course_section = CourseSection.objects.get(pk=pk)
        except CourseSection.DoesNotExist:    
            raise NotFound(detail="CourseSection not found.")
        serializer = CourseSectionSerializer(course_section)
        return Response(serializer.data)