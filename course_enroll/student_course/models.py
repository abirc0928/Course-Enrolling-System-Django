from django.db import models
from CourseSection.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import Students, StudentsCourseList
from course.models import Course
from CourseSection.models import CourseSection
from datetime import datetime
# Create your models here.
class StudentCourse(models.Model):
    student = models.ForeignKey('students.Students', on_delete=models.CASCADE)
    course_section = models.ForeignKey('CourseSection.CourseSection', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_section}"
    
@receiver(post_save, sender=StudentCourse)
def cart_total_price(sender, **kwargs):
    student_course = kwargs['instance']
    
    student = student_course.student
    course = student_course.course_section.course
    teacher = student_course.course_section.teacher
    section = student_course.course_section.section
    semister = datetime.now()
    course_fee = student_course.course_section.course.cradit * 1000
    
    StudentsCourseList.objects.create(
        student = student,
        course = course,
        teacher = teacher,
        section = section,
        semister = semister,
        course_fee = course_fee,
    )
    

    # print(student_course['course_section'], student_course['student'])
    
    # total_cart_items = CartItems.objects.filter(user = cart_items.user )
    # cart = Cart.objects.get(id = cart_items.cart.id)

    # total_price = 0
    # for item in total_cart_items:
    #     total_price += item.price
    # cart.total_price = total_price
    # cart.save()
    