from rest_framework.serializers import ModelSerializer
from .models import Rate, Personal


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


class PersonalSerializer(ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'
