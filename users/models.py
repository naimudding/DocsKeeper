from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class AccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('user must have a username.')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username= username,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class member(AbstractBaseUser):
    Gender_Choices = (
        ('Male', "Male"),
        ("female", "Female"),
    )
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=True)
    sex = models.CharField(
        max_length=6,
        choices= Gender_Choices,
        default="Male"
    )
    is_admin = models.BooleanField(default=True)
    is_active =  models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=True)
    is_superuser =  models.BooleanField(default=True)

    objects  = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username