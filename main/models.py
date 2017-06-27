from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)