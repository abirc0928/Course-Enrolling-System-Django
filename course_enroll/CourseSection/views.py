from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# from .serializers import *
# Create your views here.

class CourseSectionView(APIView):
    def get(self, request):
        course_section = CourseSection.objects.all()
        serializer = CourseSectionSerializer(course_section, many=True)
        return Response(serializer.data)
    def post(self, request):
        course = CourseSection(
            course=Course.objects.get(id=request.data["course_id"]),
            section=Sections.objects.get(id=request.data["section_id"]),
        )
        course.save()
        return Response(status=status.HTTP_201_CREATED)