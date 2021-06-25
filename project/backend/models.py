from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}. Username: {self.username}'


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=5000)
    img_url = models.URLField(null=True)
    img = models.ImageField(null=True)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, category: {self.category}'


class Course(models.Model):
    code = models.CharField(max_length=7, unique=True)
    item = models.ManyToManyField(Item, related_name='courses')

    def __str__(self):
        items = [str(item) for item in self.item.all()].join('\n')
        return f'Code: {self.code} \n, {items}'



