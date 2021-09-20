"""Circle invitation managers."""

# Django
from django.db import models

# Utilities
import random
from string import ascii_uppercase, digits

<<<<<<< HEAD
class InvitationManager(models.Manager):
    """Invitation Manager.
=======

class InvitationManager(models.Manager):
    """Invitation manager.
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29

    Used to handle code creation.
    """

    CODE_LENGTH = 10

<<<<<<< HEAD
    def create(self, **kwards):
        """Handle code creation."""
        pool = ascii_uppercase + digits + '.-'
        code = kwards.get('code',''.join(random.choices(pool, k=self.CODE_LENGTH)))
        while self.filter(code=code).exists():
            code = ''.join(random.choices(pool, k=self.CODE_LENGTH))
        kwards['code'] = code
        return super(InvitationManager, self).create(**kwards)
=======
    def create(self, **kwargs):
        """Handle code creation."""
        pool = ascii_uppercase + digits + '.-'
        code = kwargs.get('code', ''.join(random.choices(pool, k=self.CODE_LENGTH)))
        while self.filter(code=code).exists():
            code = ''.join(random.choices(pool, k=self.CODE_LENGTH))
        kwargs['code'] = code
        return super(InvitationManager, self).create(**kwargs)
>>>>>>> bbc966a9d58bf236d512eb56eb1ecf2ab5fc9f29
