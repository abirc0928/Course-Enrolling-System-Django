from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cradit = models.FloatField()

    def __str__(self):
        return self.title