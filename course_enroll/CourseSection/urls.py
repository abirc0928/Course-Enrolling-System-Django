from django.urls import path
from .views import *

urlpatterns = [
    path('course_section/', CourseSectionView.as_view(), name='index'),
]