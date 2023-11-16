from rest_framework.serializers import ModelSerializer, ReadOnlyField, ValidationError
from .models import Review, ReviewImage, Comment


class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, rating):
        if rating in range(1, 6):
            return rating
        raise ValidationError(
            'rating not be more 5'
        )

    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep



class ReviewImageSerializer(ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = "__all__"


class CommentActionSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    review = ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment