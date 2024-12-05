from rest_framework import serializers
from .models import *
from CourseSection.serializers import CourseSectionSerializer
from students.serializer import StudentSerializer
class StudentCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentCourse
        fields = '__all__'