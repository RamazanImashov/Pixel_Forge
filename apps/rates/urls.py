from rest_framework.routers import DefaultRouter
from .views import RateViewSet, PersonalViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('rate', RateViewSet)
router.register('personal', PersonalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]