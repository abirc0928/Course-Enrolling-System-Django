from django.shortcuts import render
from .models import *
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer
from rest_framework.viewsets import ModelViewSet


# # Create your views here.
# class CourseView(APIView):

#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         course = Course(
#             title=request.data["title"],
#             description=request.data["description"],
#             cradit=request.data["cradit"],
#         )
#         course.save()
#         return Response(status=status.HTTP_201_CREATED)


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    