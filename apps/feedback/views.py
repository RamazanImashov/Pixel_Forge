from rest_framework.viewsets import ModelViewSet
from .serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Review

# Create your views here.


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticatedOrReadOnly]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
