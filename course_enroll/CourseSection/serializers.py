from rest_framework import serializers
from .models import *
from course.serializers import CourseSerializer
from sections.serializers import SectionSerializer
from teachers.serializers import TeacherSerializer
from students.serializer import StudentSerializer
from students.models import Students
from student_course.models import StudentCourse
# from student_course.serializers import *


class CourseSectionSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)
    section_id = serializers.IntegerField(write_only=True)
    teacher_id = serializers.IntegerField(
        write_only=True, required=False, allow_null=True
    )  # Accept teacher_id in the request

    course = CourseSerializer(read_only=True)  # Show course details in the response
    section = SectionSerializer(read_only=True)  # Show section details in the response
    teacher = TeacherSerializer(read_only=True)  # Show teacher details in the response

    students = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CourseSection
        fields = [
            "id",
            "course_id",
            "section_id",
            "teacher_id",
            "course",
            "section",
            "teacher",
            "students",
        ]

    def get_students(self, obj):
        # Fetch students linked to this course section
        student_courses = StudentCourse.objects.filter(course_section=obj)
        students = []  # Create an empty list
        for sc in student_courses:  # Loop through the student_courses queryset
            students.append(sc.student)  # Add the `student` field of each StudentCourse to the list
            
        return StudentSerializer(students, many=True).data  

    def validate(self, data):
        request_method = self.context.get("request_method", None)
        if not Course.objects.filter(id=data.get("course_id")).exists():
            raise serializers.ValidationError("The specified course does not exist.")
        if not Sections.objects.filter(id=data.get("section_id")).exists():
            raise serializers.ValidationError("The specified section does not exist.")

        if request_method == "POST":
            existing_course_section = CourseSection.objects.filter(
                course=data["course_id"], section=data["section_id"]
            )
            if existing_course_section.exists():
                raise serializers.ValidationError(
                    "This course already has this specific section."
                )
            
        return data

    def create(self, validated_data):
        course = Course.objects.get(id=validated_data["course_id"])
        section = Sections.objects.get(id=validated_data["section_id"])
        teacher = None

        if "teacher_id" in validated_data and validated_data["teacher_id"] is not None:
            teacher = Teachers.objects.get(id=validated_data["teacher_id"])

        return CourseSection.objects.create(
            course=course, section=section, teacher=teacher
        )

    def update(self, instance, validated_data):
        if "course_id" in validated_data and instance.course_id != validated_data["course_id"]:

            existing_course_section = CourseSection.objects.filter(
                course=validated_data["course_id"], section=validated_data["section_id"]
            )
            if existing_course_section.exists():
                raise serializers.ValidationError(
                    "This course already has this specific section. Please choose a different course."
                )
            
            instance.course = Course.objects.get(id=validated_data["course_id"])
        if "section_id" in validated_data and instance.section_id != validated_data["section_id"]:

            existing_course_section = CourseSection.objects.filter(
                course=validated_data["course_id"], section=validated_data["section_id"]
            )
            if existing_course_section.exists():
                raise serializers.ValidationError(
                    "This course already has this specific section. Please choose a different section."
                )
            
            instance.section = Sections.objects.get(id=validated_data["section_id"])
        if "teacher_id" in validated_data and instance.teacher_id != validated_data["teacher_id"]:
            instance.teacher = (
                Teachers.objects.get(id=validated_data["teacher_id"])
                if validated_data["teacher_id"] is not None
                else None
            )
        instance.save()
        return instance
