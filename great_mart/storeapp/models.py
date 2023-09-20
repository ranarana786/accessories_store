"""
Models for the store app
"""
from django.db import models
from category.models import Category
from django.urls import reverse


class Product(models.Model):
    """
    Models for Products
    """
    prod_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        """
        get the url for the product and return that url
        """
        return reverse('product-detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.prod_name
