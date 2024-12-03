from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
]

routes = DefaultRouter()
routes.register("", TeacherView, basename="teacher")
urlpatterns += routes.urls