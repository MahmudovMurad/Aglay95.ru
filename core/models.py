from email.mime import image
from turtle import update
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    create_at = models.CharField(max_length=50, blank=True, null=True)
    # description = models.TextField(max_length=1000)

class BlogList(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)





class Banner(models.Model):
    title = models.CharField(max_length=200)
    image_large = models.ImageField(upload_to='images/', blank=True, null = True)
    image_small = models.ImageField(upload_to='images/', blank=True, null = True)
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)


class Subscriber(models.Model):
    """
    Email accounts
    """

    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True, blank=True)

    #moderations
    created_at = models.DateTimeField(auto_now=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.email