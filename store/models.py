from distutils.command.upload import upload
from email.mime import image
from unicodedata import name
from django.urls import reverse_lazy

from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="stone name")
    description = models.TextField(max_length=1000, verbose_name="description")
    image = models.ImageField(upload_to='images/', verbose_name="image")
    details = models.TextField(max_length=1000, verbose_name="details")

    def get_absolute_url(self):
        return reverse_lazy('post:post_detail', kwargs={
            'id': self.id
        })

class ProductDetail(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail = models.TextField(max_length=1000, verbose_name="detail")
    image = models.ImageField(upload_to='images/', verbose_name="image")
    create_at = models.DateTimeField(auto_now_add=True)

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    # subject = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)