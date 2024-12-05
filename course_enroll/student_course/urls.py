from django.urls import path
from .views import *
urlpatterns = [
    path('',StudentCourseView.as_view(), name='student_course')
]
