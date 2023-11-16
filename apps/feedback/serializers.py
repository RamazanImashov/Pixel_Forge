from rest_framework.serializers import ModelSerializer, ReadOnlyField, ValidationError
from .models import Review


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