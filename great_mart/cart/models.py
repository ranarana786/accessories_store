"""
Models for the Cart and Cart Items
"""
from django.db import models
from storeapp.models import Product


class Cart(models.Model):
    """
    Models that hold the cart for the user with session key
    """
    cart_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    """
    Models contains all the items in cart
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        """
        Total of single cart Item
        """
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.prod_name
