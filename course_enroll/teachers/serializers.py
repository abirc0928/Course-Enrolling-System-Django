from rest_framework import serializers
from .models import *
from course.serializers import CourseSerializer
from sections.serializers import SectionSerializer
from course.models import Course
from sections.models import Sections


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'