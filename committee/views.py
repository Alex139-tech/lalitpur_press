from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,CreateModelMixin
from .models import Member,Position
from .serializers import MemberSerializer,PositionSerializer

class MemberViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet,CreateModelMixin):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
