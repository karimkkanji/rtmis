from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import signing
from django.db import models

# Create your models here.
from utils.custom_manager import UserManager


class SystemUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_sign_pk(self):
        return signing.dumps(self.pk)

    class Meta:
        db_table = "system_user"
