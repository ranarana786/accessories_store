""""
Models for the User creation and Managing all the user operation in the project
"""

from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Manage all the operations from simple to superuser creation
    """

    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Create the simple user
        """
        if not email:
            raise ValueError('Email Must Be Provided')
        if not username:
            raise ValueError('UserName Must Be Provided')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    """
    Model for the custom user
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=50, default='nick_name')

    date_joined = models.DateTimeField(auto_now_add=True, editable=True)
    last_login = models.DateTimeField(auto_now_add=True, editable=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
