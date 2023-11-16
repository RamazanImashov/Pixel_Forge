from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Project, ProjectImage


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ProjectImageSerializer(instance.project.all(), many=True).data
        return rep


class ProjectImageSerializer(ModelSerializer):
    # project = ReadOnlyField()

    class Meta:
        model = ProjectImage
        fields = "__all__"

    # def create(self, validated_data):
    #     image = ProjectImage.objects.create(**validated_data)
    #     return image
