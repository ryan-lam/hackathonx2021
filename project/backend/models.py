from django.db import models

# Create your models here.

class Item(models.Model):
    id_ = models.CharField(max_length="200", required=True)
    name = models.CharField(max_length="200")
    art_type = models.CharField(max_length="200")
    img = models.ImageField()

class Course(models.Model):
    code = models.OneToOneField()
    sequence = models.ExpressionList
