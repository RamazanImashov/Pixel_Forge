from rest_framework.viewsets import ModelViewSet
from .models import ProjectImage, Project
from .serializers import ProjectSerializer, ProjectImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticatedOrReadOnly]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    # @action(methods=['POST'], detail=True, permission_classes=[IsAdminUser])
    # def images(self, request, pk=None):
    #     project = self.get_object()
    #     serializer = ProjectImageSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(project=project)
    #         message = request.data
    #         return Response(message, status=200)


class ProjectImageViewSet(ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAdminUser]
