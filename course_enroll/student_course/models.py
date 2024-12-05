from django.db import models
from CourseSection.models import *
# Create your models here.
class StudentCourse(models.Model):
    student = models.ForeignKey('students.Students', on_delete=models.CASCADE)
    course_section = models.ForeignKey('CourseSection.CourseSection', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_section}"
    