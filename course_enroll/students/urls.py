from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import * 

urlpatterns = [
    # path("student/", StudentView.as_view(), name="student"),
]

routers = DefaultRouter()
routers.register("", StudentView, basename="student")

urlpatterns += routers.urls