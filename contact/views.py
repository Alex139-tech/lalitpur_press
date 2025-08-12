from django.shortcuts import render
from rest_framework.response import Response
from .models import Contact,Report
from .serilizers import ContactSerilizer,ReportSerilizers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import  RetrieveModelMixin,CreateModelMixin,ListModelMixin
# Create your views here.

class ContactViewSet(CreateModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerilizer


class ReportViewSet(CreateModelMixin, GenericViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerilizers
