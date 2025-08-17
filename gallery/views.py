from django.shortcuts import render
from .models import PhotoGallery
from .serilizers import GallerySerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
# Create your views here.

class GalleryViewSet(GenericViewSet,RetrieveModelMixin,ListModelMixin,):
    queryset = PhotoGallery.objects.all()
    serializer_class = GallerySerializer