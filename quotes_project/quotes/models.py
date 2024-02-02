from django.db import models

# Create your models here


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    app_label = "quotes"

    def __str__(self):
        return self.text
