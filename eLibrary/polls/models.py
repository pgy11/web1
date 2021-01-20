from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, primary_key=True, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)

class 