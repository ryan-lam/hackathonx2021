from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default="Dinosaurs")
    description = models.CharField(max_length=5000)
    description = models.TextField()
    img_url = models.URLField(null=True, blank=True)
    img = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, category: {self.category}'

class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return f'{self.name}. Username: {self.username}'

class Course(models.Model):
    code = models.CharField(max_length=7, unique=True)
    items = models.ManyToManyField(Item, related_name='courses', through='Sequence')

    def __str__(self):
        # items = '\n'.join([str(item) for item in self.item.all()])
        return f'Code: {self.code} \n'


class Sequence(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    index = models.IntegerField()

    def __str__(self):
        return f'Course: {self.course.code}, index: {self.index}, Item: {self.item.name}'


class DiscussionPost(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    post = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'{self.post}. BY {self.user.name}. POSTED ON {self.time.month}/{self.time.day} TO {self.item.name}'

class SavedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return f'{self.item.name}. Saved by {self.user.name}'