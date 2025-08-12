from rest_framework import serializers
from .models import Contact,Report

class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','subject','message','phone','email']


class ReportSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['name','subject','message','phone','email','address','screenshot','aavedan','document']
        