"""
Contain all models that hold information for categories
"""
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Category Model contain fields for single category
    """
    category_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/category', blank=True)

    class Meta:
        """
        set the meta information for model
        """
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('get_product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name
