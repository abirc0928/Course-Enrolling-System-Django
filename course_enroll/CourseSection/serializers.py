from rest_framework import serializers
from .models import *
from course.serializers import CourseSerializer
from sections.serializers import SectionSerializer
from teachers.serializers import TeacherSerializer
class CourseSectionSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)  # Accept course_id in the request
    section_id = serializers.IntegerField(write_only=True)  # Accept section_id in the request
    teacher_id = serializers.IntegerField(write_only=True)  # Accept teacher_id in the request

    course = CourseSerializer(read_only=True)  # Show course details in the response
    section = SectionSerializer(read_only=True)  # Show section details in the response
    teacher = TeacherSerializer(read_only=True)  # Show teacher details in the response
    class Meta:
        model = CourseSection
        fields = ['id', 'course_id', 'section_id', 'teacher_id','course', 'section', 'teacher']
        

    def validate(self, data):

        if not Course.objects.filter(id=data.get('course_id')).exists():
            raise serializers.ValidationError("The specified course does not exist.")
        if not Sections.objects.filter(id=data.get('section_id')).exists():
            raise serializers.ValidationError("The specified section does not exist.")
        if not Teachers.objects.filter(id=data.get('teacher_id')).exists():
            raise serializers.ValidationError("The specified Teacher does not exist.")
        return data

    def create(self, validated_data):
        course = Course.objects.get(id=validated_data['course_id'])
        section = Sections.objects.get(id=validated_data['section_id'])
        teacher = Teachers.objects.get(id=validated_data['teacher_id'])
        print(course, section, teacher)
        if CourseSection.objects.filter(course=course, section=section, teacher=teacher).exists():
            print("The course and section combination already exists.")
            raise serializers.ValidationError("The course and section combination already exists.")
        print("done")
        return CourseSection.objects.create(course=course, section=section, teacher=teacher)
    
