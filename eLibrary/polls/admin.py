from django.contrib import admin
from .models import UserInfo, Book

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Book)