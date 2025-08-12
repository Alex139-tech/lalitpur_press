from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import Member,Position
from .serlilizers import MemberSerializer,PositionSerializer

class MemberViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
