from django.db import models
from django.contrib.auth.models import User
from django.db.models import F


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def increase_popularity(self):
        Tag.objects.filter(id=self.id).update(popularity=F("popularity") + 1)


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    book = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    content = models.TextField(default="")
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text
