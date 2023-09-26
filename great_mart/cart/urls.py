"""
All the Urls for the Cart APP
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name='cart'),
    path('add-to-cart/<int:product_id>', views.add_cart, name='add-to-cart'),
    path('decrease-quantity/<int:product_id>', views.decrease_quantity, name='decrease-quantity'),
    path('remove-cart-item/<int:cart_item_id>', views.remove_cart_item, name='remove-cart-item')
]
