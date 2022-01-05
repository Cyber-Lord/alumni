from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, User, BaseUserManager,  AbstractBaseUser
from django.db.models.base import Model

from . constants import GENDER, SCHOOL_TYPES

class School(models.Model):

    school_name = models.CharField(max_length=255)
    school_motto = models.CharField(max_length=255)
    school_logo = models.ImageField(upload_to='logos/', blank=False)
    school_phone = models.CharField(max_length=15, blank=True, null=True)
    school_address = models.TextField()
    school_website = models.CharField(max_length=50)
    school_type = models.CharField(max_length=255, choices=SCHOOL_TYPES)

    def __str__(self) -> str:
        return self.school_name

class Student(models.Model):
    email = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER, default='MALE')
    photo = models.ImageField(upload_to='photos/', blank=True)
    address = models.TextField()
    lga = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    dob = models.DateField()
    quote = models.TextField()
    best_friend = models.CharField(max_length=255)
    best_moment = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be \
         entered in the format: '+234 ...'")
    phone_no = models.CharField(validators=[phone_regex], max_length=15, blank=False)