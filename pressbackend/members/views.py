from django.shortcuts import render
from .models import Member
from .serlilizers import MemberSerilizers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import  RetrieveModelMixin,ListModelMixin
# Create your views here.



class MemererViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerilizers