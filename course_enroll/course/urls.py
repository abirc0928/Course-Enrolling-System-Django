from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    # path("course/", CourseView.as_view(), name="course"),
]

routers = DefaultRouter()
routers.register("", CourseViewSet, basename="course_section")

urlpatterns += routers.urls