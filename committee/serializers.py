from rest_framework import serializers
from .models import Position, Member

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'title']


class MemberSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(), source='position', write_only=True
    ) 

    class Meta:
        model = Member
        fields = [
            'id',
            'profile_picture',
            'name',
            'bio',
            'email',
            'contact_number',
            'quotation',
            'member_type',
            'position',
            'position_id',
            'joined_date',
        ]
