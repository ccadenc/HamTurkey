# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Your name should be more than 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Blog desc should be more than 8 characters"
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()


class Quotes(models.Model):
    user = models.CharField(max_length=255)
    Desc = models.TextField(max_length=2000)


class Favoirtes(models.Model):
    user = models.CharField(max_length=255)


    # one to many
user = models.ForeignKey(User, related_name="quotes")

# many to many
users = models.ManyToManyField(Favorites, related_name="favorites")


def __str__(self):
    return self.email
