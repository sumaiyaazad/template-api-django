#
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
#     PermissionsMixin
#
#
# class UserManager(BaseUserManager):
#     pass
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """Custom user model that suppors using email instead of username"""
#     email = models.EmailField(max_length=255, unique=True)
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
