"""Circles permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from cride.circles.models import Membership


class IsActiveCircleMember(BasePermission):
    """Allow access only to circle members.

    Expect that the views implementing this permission
    have a `circle` attribute assigned.
    """

    def has_permission(self, request, view):
        """Verify user is an active member of the circle."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True


class IsSelfMember(BasePermission):
<<<<<<< HEAD
    """Allow access only to members owners."""

    def has_object_permission(self, request, view, obj):
        """Let object permission grant access"""
=======
    """Allow access only to member owners."""

    def has_permission(self, request, view):
        """Let object permission grant access."""
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow access only if member is owned by the requesting user."""
<<<<<<< HEAD
        return request.user == obj.user
=======
        return request.user == obj.user
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
