"""Circles permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

<<<<<<< HEAD
# Model
from cride.circles.models import Membership

class IsCircleAdmin(BasePermission):
    """Allows access only to circle admins."""
=======
# Models
from cride.circles.models import Membership


class IsCircleAdmin(BasePermission):
    """Allow access only to circle admins."""
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29

    def has_object_permission(self, request, view, obj):
        """Verify user have a membership in the obj."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=obj,
                is_admin=True,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True
