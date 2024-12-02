from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from .views import * 

urlpatterns = [
    # path("section/", SectionView.as_view(), name="section"),
]

routes = DefaultRouter()
routes.register("", SectionViewSet, basename="section")
urlpatterns += routes.urls