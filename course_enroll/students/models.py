from django.db import models

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