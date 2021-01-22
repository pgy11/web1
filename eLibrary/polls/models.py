from django.db import models


class UserInfo(models.Model):
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, primary_key=True, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=20, null=False, blank=False)
    objects = models.Manager()

