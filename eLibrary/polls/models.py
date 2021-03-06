from django.db import models


class UserInfo(models.Model):
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, primary_key=True, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=20, null=False, blank=False)
    objects = models.Manager()


class Book(models.Model):
    image_URL = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    edition = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, primary_key=True, null=False, blank=False)
    rating = models.FloatField()
    objects = models.Manager()

