from rest_framework import serializers,generics
from .models import *

class TagSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = '__all__'
        # depth = 1

class ImageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    class Meta:
        model = Image
        fields = '__all__'
        depth = 1

