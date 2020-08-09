from django.test import TestCase
from .models import User,Post,tags

# Create your tests here.
class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.john= User(first_name = 'John', last_name ='Doe', email ='john@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.john,User)) 


class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()