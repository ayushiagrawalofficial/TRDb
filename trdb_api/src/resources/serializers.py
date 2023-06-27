from rest_framework import serializers

from resources.models import StudyResource, Technology, Vote


class StudyResourceSerializer(serializers.ModelSerializer):
    """Study Resource Serializer"""

    class Meta:
        model = StudyResource
        exclude = ["user"]


class TechnologySerializer(serializers.ModelSerializer):
    """Technology Serializer"""

    class Meta:
        model = Technology
        exclude = ["user"]


class VoteSerializer(serializers.ModelSerializer):
    """Vote Serializer"""

    class Meta:
        model = Vote
        exclude = ["user"]
