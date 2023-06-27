from django_filters import rest_framework as filters

from resources.models import StudyResource, Technology, Vote


class StudyResourceFilterSet(filters.FilterSet):
    """Study Resource Filter Set"""

    order = filters.OrderingFilter(fields=("created", "title", "vote_count"))

    class Meta:
        model = StudyResource
        fields = ["technology"]


class TechnologyFilterSet(filters.FilterSet):
    """Technology Filter Set"""

    order = filters.OrderingFilter(fields=("name",))

    class Meta:
        model = Technology
        fields = ["technology_type"]


class VoteFilterSet(filters.FilterSet):
    """Vote Filter Set"""

    class Meta:
        model = Vote
        fields: list[str] = []
