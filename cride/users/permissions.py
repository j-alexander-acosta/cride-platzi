"""User permissions."""

<<<<<<< HEAD
# Django rest framework
=======
# Django REST Framework
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
<<<<<<< HEAD
        """Check object and user are the same."""
        return request.user == obj
=======
        """Check obj and user are the same."""
        return request.user == obj
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
