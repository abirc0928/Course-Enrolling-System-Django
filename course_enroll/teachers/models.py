from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name