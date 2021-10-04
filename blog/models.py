from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
