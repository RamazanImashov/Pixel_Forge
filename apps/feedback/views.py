from rest_framework.viewsets import ModelViewSet, generics
from .serializers import RatingSerializer, ReviewImageSerializer, CommentActionSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Review, ReviewImage
from .permissions import IsAuthorPermission
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class ProjectImageView(generics.CreateAPIView):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer
    permission_classes = [IsAuthorPermission]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permissions = [IsAuthenticatedOrReadOnly]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def comments(self, request, pk=None):
        review = self.get_object()
        user = request.user
        serializer = CommentActionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, author=user)
            message = request.data
            return Response(message, status=200)
