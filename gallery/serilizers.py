from rest_framework import serializers
from .models import PhotoGallery, GalleryImage

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']  

class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = PhotoGallery
        fields = ['id', 'feature_image', 'title', 'images']
