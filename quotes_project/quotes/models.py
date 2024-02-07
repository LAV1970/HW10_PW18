from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
