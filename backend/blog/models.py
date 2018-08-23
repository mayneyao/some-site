# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=64, unique=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=128)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    publish_on = models.DateTimeField()
