from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password, **extra_fields):
        if not email:
            raise TypeError('The Email field must be set.')
        if not fullname:
            raise TypeError('Full name is required.')
        if not password:
            raise TypeError('Password is required.')
        if not extra_fields.get("phone_number"):
            raise TypeError('Phone number is required.')
        user = self.model(email=self.normalize_email(email), fullname=fullname, phone_number=extra_fields.get("phone_number"))
        user.set_password(password)
        user.save()
        return user

    def super_user(self, email, password, **extra_fields):
        if not email:
            raise TypeError('The Email field must be set.')
        if not password:
            raise TypeError('Password is required.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.super_user = True
        user.save()
        return user

ACCOUNT_TYPE = [
    ('BUYER', 'Buyer'),
    ('SELLER', 'Seller'),
    ('RIDER', 'Rider'),
    ('ADMIN', 'Admin')
]