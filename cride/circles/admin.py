"""Circles admin."""

# Django
from django.contrib import admin

<<<<<<< HEAD
# Models
=======
# Model
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
<<<<<<< HEAD
        'members_limit',
    )
    search_fields = (
        'slug_name',
        'name'
    )
=======
        'members_limit'
    )
    search_fields = ('slug_name', 'name')
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
    list_filter = (
        'is_public',
        'verified',
        'is_limited'
<<<<<<< HEAD
    )
=======
    )
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
