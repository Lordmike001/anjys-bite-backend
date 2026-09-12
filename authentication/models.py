from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
import uuid

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password, **extra_fields):
        if not email:
            raise TypeError("The Email field must be set.")
        if not fullname:
            raise TypeError("Full name is required.")
        if not password:
            raise TypeError("Password is required.")
        if not extra_fields.get("phone_number"):
            raise TypeError("Phone number is required.")
        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            phone_number=extra_fields.get("phone_number"),
        )
        user.set_password(password)
        user.save()
        return user

    def super_user(self, email, password, **extra_fields):
        if not email:
            raise TypeError("The Email field must be set.")
        if not password:
            raise TypeError("Password is required.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = True
        user.super_user = True
        user.save()
        return user


ACCOUNT_TYPE = [
    ("BUYER", "Buyer"),
    ("SELLER", "Seller"),
    ("RIDER", "Rider"),
    ("ADMIN", "Admin"),
]


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(unique=True)
    address = models.CharField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    bvn = models.CharField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname','phone_number']
    objects = UserManager()
    
    
    def __str__(self):
        return self.fullname