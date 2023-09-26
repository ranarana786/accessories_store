from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from storeapp.models import Product
from .models import (CartItem, Cart)


def _get_cart_id(request):
    """
    Get the cart_id if Null then add New One
    """
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def add_cart(request, product_id):
    """
    views that will add the item in cart
    """

    # color = request.GET['color']
    # size = request.GET['size']
    #
    # return HttpResponse(
    #     f"{size} and the color is {color}"
    # )
    product = Product.objects.get(id=product_id)

    # print(product_id)
    # print("the product is the -----", product)

    try:
        """
        it will check if the cart exist then get that cart else create new one
        """
        cart = Cart.objects.get(cart_id=_get_cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_get_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(
            cart=cart,
            product=product
        )
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=1
        )
        cart_item.save()

    return redirect('cart')


def cart_page(request, total=0, quantity=0, cart_items=None):
    """
    Show the template of the cart page
    """
    cart_id = _get_cart_id(request)
    print(cart_id)
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)

    # print(cart.cart_id)
    # print(type(cart_items))

    for cart_item in cart_items:
        total = total + (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (3 * total) / 100
    grand_total = total + tax

    # print(total)
    # print(quantity)

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'cart/cart_page.html', context=context)


def decrease_quantity(request, product_id):
    # print(product_id)
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=_get_cart_id(request))

    # print(product.prod_name)
    # print(cart.cart_id)

    cart_item = CartItem.objects.filter(cart=cart, product=product)[0]
    print(cart_item)

    cart_item.quantity = cart_item.quantity - 1
    cart_item.save()

    return redirect('cart')


def remove_cart_item(request, cart_item_id):
    print(cart_item_id)
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    print(cart_item)
    return redirect('cart')
