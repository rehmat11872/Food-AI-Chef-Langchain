from django.contrib.auth.hashers import make_password
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUser(AbstractBaseUser):

    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    # required
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, add_label):
        return True

    # def save(self, *args, **kwargs):
    #     # Hash the password if it's set and not hashed already
    #     if self.password and not self.password.startswith("pbkdf2_sha256$"):
    #         self.password = make_password(self.password)
    #     super(User, self).save(*args, **kwargs)
