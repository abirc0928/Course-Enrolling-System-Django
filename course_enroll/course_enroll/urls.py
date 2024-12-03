
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/course/', include('course.urls')),
    path('api/sections/', include('sections.urls')),
    path('api/', include('CourseSection.urls')),
    path('api/teachers/', include('teachers.urls')),
    path('api/students/', include('students.urls')),
]
