from django.shortcuts import render
from rest_framework.response import Response
from .models import News,Notice
from .serilizers import NewsSerilizers,NoticeSerilizers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import  RetrieveModelMixin,ListModelMixin
# Create your views here.

class NewsViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerilizers


class NoticeViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerilizers
