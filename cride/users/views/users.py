<<<<<<< HEAD
"""User views."""
=======
"""Users views."""
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from cride.users.permissions import IsAccountOwner

# Serializers
from cride.users.serializers.profiles import ProfileModelSerializer
from cride.circles.serializers import CircleModelSerializer
from cride.users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Models
from cride.users.models import User
<<<<<<< HEAD
from cride .circles.models import Circle
=======
from cride.circles.models import Circle

>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """
<<<<<<< HEAD
=======

>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
<<<<<<< HEAD
            permissions = [('AllowAny')]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permissions = [(IsAuthenticated, IsAccountOwner)]
        else:
            permissions = [('IsAuthenticated')]
=======
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
<<<<<<< HEAD
        user, token  = serializer.save()
=======
        user, token = serializer.save()
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

<<<<<<< HEAD

=======
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

<<<<<<< HEAD

=======
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now go share some rides!'}
        return Response(data, status=status.HTTP_200_OK)

<<<<<<< HEAD
    @action(detail=True, methods=['put','patch'])
=======
    @action(detail=True, methods=['put', 'patch'])
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        circles = Circle.objects.filter(
            members=request.user,
            membership__is_active=True
        )
        data = {
            'user': response.data,
            'circles': CircleModelSerializer(circles, many=True).data
        }
        response.data = data
<<<<<<< HEAD
        return response
=======
        return response
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
