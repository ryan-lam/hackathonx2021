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
    category = models.CharField(max_length=200, default="Dinosaurs")
    description = models.CharField(max_length=5000)
    description = models.TextField()
    img_url = models.URLField(null=True, blank=True)
    img = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, category: {self.category}'


class Course(models.Model):
    code = models.CharField(max_length=7, unique=True)
    item = models.ManyToManyField(Item, related_name='courses')

    def __str__(self):
        items = '\n'.join([str(item) for item in self.item.all()])
        return f'Code: {self.code} \n, {items}'



