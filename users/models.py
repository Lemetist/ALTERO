import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    image = models.ImageField(upload_to='advertisements/%Y/%m/%d', null=True, blank=True)




class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='advertisements/%Y/%m/%d')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact_info = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']


