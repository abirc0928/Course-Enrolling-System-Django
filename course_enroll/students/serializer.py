from rest_framework import serializers
from .models import *
from course.serializers import CourseSerializer
from sections.serializers import SectionSerializer
from teachers.serializers import TeacherSerializer
from CourseSection.models import CourseSection  # Import only the model here
from student_course.models import StudentsCourseList
from students.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"



class StudentCourseSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField(read_only=True)
    payment_due = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Students
        fields = ["id", "name", "email", "admitions_semester", "department","completed_cradit","payment_due",  "courses"]

    def get_courses(self, obj):
        # Fetch the courses associated with this student
        courses = StudentsCourseList.objects.filter(student=obj)
        course_data = []

        for course in courses:
            course_data.append(
                {
                    "title": course.course.title,
                    "description": course.course.description,
                    "cradit": course.course.cradit,
                    "course_fee": course.course_fee,
                    "course_status": course.course_status,
                    "course_payment" : course.course_payment,
                    "section": {
                        "section_name": course.section.section_name,
                        "schedule":  course.section.schedule,  
                        "capacity": course.section.capacity,  
                    },
                    "teacher": {
                        "name": course.teacher.name,
                        "email": course.teacher.email,  
                        "phone": course.teacher.phone,  
                        "department": course.teacher.department,  
                    },
                }
            )
        return course_data
    def get_payment_due(self ,obj):

        courses = StudentsCourseList.objects.filter(student=obj)
        total = 0

        for course in courses:
            if course.course_payment == False:
                total = total + course.course_fee

            if course.course_payment == True:
                course.course_status = "Ongoing"
                course.save()
        return total

