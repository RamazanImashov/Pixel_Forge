from django.urls import path, include
from .views import (
    RegisterView,
    ActivationViewCode,
    UsersView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UsersView)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('activate_code/', ActivationViewCode.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


