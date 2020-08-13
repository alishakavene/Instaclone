from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# create models here


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
