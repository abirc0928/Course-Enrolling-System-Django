from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from students.models import *

# Create your views here.
class StudentCourseView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_course = StudentCourse.objects.all()
        serializer = StudentCourseSerializer(student_course, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        try:
            student = Students.objects.get(id=request.data["students"])
            course_section = CourseSection.objects.get(id=request.data["course_section"])
        
            student_course = StudentCourse(
                student=student,
                course_section=course_section,
            )
            student_course.save()
            serializers = StudentCourseSerializer(student_course, many=False)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
            
        except Students.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        except CourseSection.DoesNotExist:
            return Response({"error": "CourseSection not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)