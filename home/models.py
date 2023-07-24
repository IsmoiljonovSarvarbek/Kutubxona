from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     id = models.BigAutoField(primary_key=True)

class AdminProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,related_name='admin')

class Jadval(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Books', on_delete=models.CASCADE)
    status = models.IntegerField()
    admin = models.ForeignKey('AdminProfile', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.CharField(max_length=255, null=True)
    rating = models.IntegerField(null=True)

class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.CharField(max_length=255)
    status = models.BooleanField()
    isbn = models.BigIntegerField()

