from tkinter import CASCADE
from django.db import models
from django.db.models.base import Model

# Create your models here.

class AuthorRegister(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.TextField(max_length=50)
    age = models.PositiveIntegerField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    author=models.CharField(default='NA', max_length=30)

    def __str__(self) -> str:
        return self.title