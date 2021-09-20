"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cride.users.models import Profile

<<<<<<< HEAD
=======

>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'biography',
            'rides_taken',
            'rides_offered',
            'reputation'
        )
        read_only_fields = (
            'rides_taken',
            'rides_offered',
            'reputation'
        )
