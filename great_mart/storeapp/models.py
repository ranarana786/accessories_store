"""
Models for the store app
"""
from django.db import models
from category.models import Category
from django.urls import reverse



variation_category_choices = (
    ('color', 'color'),
    ('size', 'size'),
)


class ProductVariations(models.Model):
    """
    Model for the product variations
    """
    variations = models.CharField(max_length=255, choices=variation_category_choices)
    value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.variations} + {self.value}"




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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    variations = models.ForeignKey(ProductVariations, on_delete=models.CASCADE, default=1)

    def get_url(self):
        """
        get the url for the product and return that url
        """
        return reverse('product-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.prod_name
