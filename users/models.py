from django.db import models

from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    status = models.BooleanField(default=False)
    grade = models.CharField('Grade', max_length=100)
    title = models.CharField('Title', max_length=100)
    phone = PhoneNumberField('Phone', null=True, blank=True, unique=True)
    salary = models.PositiveIntegerField('Salary')