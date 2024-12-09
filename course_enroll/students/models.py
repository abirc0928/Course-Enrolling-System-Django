from django.db import models
from course.models import Course
from CourseSection.models import CourseSection
from sections.models import *
from teachers.models import *
# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    admitions_semester = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    completed_cradit = models.FloatField(default=0, null=True, blank=True)
    completed_courses = models.TextField(default='[]', null=True, blank=True)

    def __str__(self):
        return self.name
    

class StudentsCourseList(models.Model):
    STATUS_CHOICES = [
        ("ongoing", "Ongoing"),
        ("pass", "Pass"),
        ("fall", "Fall"),
        ("withdraw", "Withdraw"),
        ("complete", "Complete"),
        ("enroll", "Enroll"),
    ]

    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    semister = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers , on_delete=models.CASCADE)
    course_status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="enroll")
    course_fee = models.FloatField(default=0, null=True, blank=True)
    course_payment = models.BooleanField(default=False, null=True, blank=True)
    

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
    

    
#     "[
#     {
#         "id": 53,
#         "student": {
#             "id": 1,
#             "name": "John Doe",
#             "email": "johndoe@example.com",
#             "admitions_semester": "Fall 2023",
#         },
#         "course": {
#             [
#                 {
#                     "id": 4,
#                     "title": "Introduction to Marketing",
#                     "description": "Covers the basics of marketing, including strategies, consumer behavior, and market analysis.",
#                     "cradit": 3.0,
#                     "section": {
#                         "id": 1,
#                         "section_name": "Section A",
#                         "schedule": "Monday, 10:00 AM - 12:00 PM",
#                         "capacity": 30,
#                     },
#                     "teacher": {
#                         "id": 1,
#                         "name": "John Doe",
#                         "email": "johndoe@example.com",
#                         "phone": "+1234567890",
#                         "department": "Computer Science",
#                     },
#                 },
#                 {
#                     "id": 5,
#                     "title": "Introduction to Marketing",
#                     "description": "Covers the basics of marketing, including strategies, consumer behavior, and market analysis.",
#                     "cradit": 3.0,
#                     "section": {
#                         "id": 1,
#                         "section_name": "Section A",
#                         "schedule": "Monday, 10:00 AM - 12:00 PM",
#                         "capacity": 30,
#                     },
#                     "teacher": {
#                         "id": 1,
#                         "name": "John Doe",
#                         "email": "johndoe@example.com",
#                         "phone": "+1234567890",
#                         "department": "Computer Science",
#                     },
#                 },
#                 {
#                     "id": 6,
#                     "title": "Introduction to Marketing",
#                     "description": "Covers the basics of marketing, including strategies, consumer behavior, and market analysis.",
#                     "cradit": 3.0,
#                     "section": {
#                         "id": 1,
#                         "section_name": "Section A",
#                         "schedule": "Monday, 10:00 AM - 12:00 PM",
#                         "capacity": 30,
#                     },
#                     "teacher": {
#                         "id": 1,
#                         "name": "John Doe",
#                         "email": "johndoe@example.com",
#                         "phone": "+1234567890",
#                         "department": "Computer Science",
#                     },
#                 },
#             ]
#         },
#     }
# ]
# "