from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length="64", unique=True)
    password = models.CharField(max_length="64")
    name = models.CharField(max_length="64")

class Item(models.Model):
    name = models.CharField(max_length="200")
    category = models.CharField(max_length="200", null=True)
    description = models.CharField(max_length="3000")
    img = models.ImageField()

class Course(models.Model):
    code = models.OneToOneField()
    sequence = models.ExpressionList



