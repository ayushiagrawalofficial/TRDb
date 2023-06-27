from rest_framework import viewsets

from resources.filters import StudyResourceFilterSet, TechnologyFilterSet, VoteFilterSet
from resources.models import StudyResource, Technology, Vote
from resources.serializers import (
    StudyResourceSerializer,
    TechnologySerializer,
    VoteSerializer,
)


class StudyResourceViewSet(viewsets.ModelViewSet):
    """Study Resource View Set"""

    queryset = StudyResource.objects.filter(is_active=True)
    serializer_class = StudyResourceSerializer
    filterset_class = StudyResourceFilterSet

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TechnologyViewSet(viewsets.ModelViewSet):
    """Technology View Set"""

    queryset = Technology.objects.filter(is_active=True)
    serializer_class = TechnologySerializer
    filterset_class = TechnologyFilterSet

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VoteViewSet(viewsets.ModelViewSet):
    """Vote View Set"""

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filterset_class = VoteFilterSet

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
