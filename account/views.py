from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ActivationSerializer,
    UsersSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsAuthorPermission

User = get_user_model()


class UsersView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthorPermission, IsAdminUser]


class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Good, Registration successful', status=201)


class ActivationViewCode(APIView):
    @swagger_auto_schema(request_body=ActivationSerializer)
    def post(self, request):
        serializer = ActivationSerializer(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response(
                'Account Successfully Activate'
            )


class LoginViewEmail(ObtainAuthToken):
    serializer_class = LoginSerializer
