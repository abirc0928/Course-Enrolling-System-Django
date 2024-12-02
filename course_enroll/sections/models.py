from django.db import models
from course.models import Course

# Create your models here.
class Sections(models.Model):
    section_name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.section_name