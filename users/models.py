from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class member(AbstractBaseUser):
    Gender_Choices = (
        ('Male', "Male"),
        ("female", "Female"),
    )

    member_name = models.CharField(max_length=20)
    member_age = models.IntegerField()
    member_phn_no = models.IntegerField()
    member_sex = models.CharField(
        max_length=6,
        choices= Gender_Choices,
        default="Male"
    )