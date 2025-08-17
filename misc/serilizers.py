from rest_framework import serializers
from .models import Publication,QR


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title','published_date','file']  




class QSerializer(serializers.ModelSerializer):
    class Meta:
        model = QR
        fields = ['qr_image',]  