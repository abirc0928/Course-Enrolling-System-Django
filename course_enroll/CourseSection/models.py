from django.db import models
from course.models import Course
from sections.models import Sections
# Create your models here.
class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.course.title} - {self.section.section_name}"