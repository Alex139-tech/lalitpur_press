from .models import Member
from rest_framework import serializers



class MemberSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['profile_picture','name','bio','role','contact_number','joined_date']

