"""Circle serializers."""

# Django REST Framework
from rest_framework import serializers

<<<<<<< HEAD
# Models
=======
# Model
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):
    """Circle model serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=32000
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        """Meta class."""

        model = Circle
        fields = (
            'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'rides_taken',
            'verified', 'is_public',
<<<<<<< HEAD
            'is_limited', 'members_limit',
=======
            'is_limited', 'members_limit'
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
        )
        read_only_fields = (
            'is_public',
            'verified',
            'rides_offered',
            'rides_taken',
        )

    def validate(self, data):
        """Ensure both members_limit and is_limited are present."""
        members_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False)
        if is_limited ^ bool(members_limit):
<<<<<<< HEAD
            raise serializers.ValidationError('If circle is limited, a member limit must be provided.')
=======
            raise serializers.ValidationError('If circle is limited, a member limit must be provided')
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
        return data
