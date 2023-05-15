from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from .manager import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True)
    born_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    #is_admin = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=True, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountManager()

    @property
    def is_staff(self):
        return self.is_superuser