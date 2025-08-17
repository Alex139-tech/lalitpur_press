from django.shortcuts import render
from .models import Publication,QR
from rest_framework.generics import RetrieveAPIView
from .serilizers import PublicationSerializer,QSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PublicationViewSet(GenericViewSet,RetrieveModelMixin,ListModelMixin):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
 

class QrView(APIView):
    def get(self,request):
        qr = QR.objects.latest()
        if qr and qr.qr_image:
            return Response({'qr_image': request.build_absolute_uri(qr.qr_image.url)})
        else:
            return Response({'error': 'QR image not found'}, status=404)

