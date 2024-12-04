from django.urls import path
from .views import *

urlpatterns = [
    path('course_section/', CourseSectionView.as_view(), name='couter_section'),
    path('course_section/<int:pk>/', CourseSectionViewDetails.as_view(), name='course_section_details'),
]