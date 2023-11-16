from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProjectViewSet, ProjectImageViewSet


router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('add_image_project', ProjectImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]