from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime


class CommonUserOperationField(models.Model):
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("updated At", auto_now=True)
    # updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


# Create your models here.
class Auth(CommonUserOperationField):
    name = models.CharField('Name', null=False, blank=False)
    is_active = models.BooleanField('Is Active', default=False)
    description = models.TextField('Description', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Category(CommonUserOperationField):
    name = models.CharField('Name', null=False, blank=False)

    def __str__(self):
        return self.name


class Item(CommonUserOperationField):
    name = models.CharField('Name', unique=True, null=False, blank=False)
    description = models.TextField('Description', blank=True, null=True)
    auther = models.ManyToManyField(Auth)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return " {} ".format(self.name)

class BaseUser(AbstractUser):
    phone_number = models.CharField("phone Number", blank=True, null=True)
    linkdin = models.URLField("linkdin", blank=True, null=True)

    def __str__(self):
        return self.username + " " + self.email