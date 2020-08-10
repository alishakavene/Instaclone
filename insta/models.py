from django.db import models
import datetime as dt


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')

    @classmethod
    def todays_posts(cls):
        today = dt.date.today()
        posts = cls.objects.filter(pub_date__date = today)
        return posts
    @classmethod
    def days_posts(cls,date):
        posts = cls.objects.filter(pub_date__date = date)
        return posts

    @classmethod
    def search_by_title(cls,search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts
