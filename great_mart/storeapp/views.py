"""
All the views that will hold the logic for handling products in store
"""
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from .models import Product
from category.models import Category


class AllProductsListView(ListView):
    """
    List View For displaying the products on the home page
    """
    model = Product
    template_name = 'home.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        """
        Method that will extract all the objects from the Products tabel
        """
        query_set = Product.objects.all().filter(is_available=True)
        return query_set


class StoreProductListView(ListView):
    """
    List Out All The Store Product
    """
    model = Product
    template_name = 'storeapp/store_page.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        """
        Extract all the objects from the database based on the conditions
        """
        query_set = Product.objects.all()
        return query_set

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Add the things in context dict and return to context_object_name variable by appending all data in
        """
        context = super().get_context_data(**kwargs)
        prod_count = Product.objects.all()
        context['products'] = prod_count.count()
        return context


def get_product_by_category(request, slug=None):
    """
    The Function Will Extract The product on Category base or return all id slug None
    """
    categories = None
    all_products = None
    if slug is None:
        all_products = Product.objects.all()
        products = all_products.count()
    else:
        category = get_object_or_404(Category, slug=slug)
        all_products = Product.objects.filter(category=category, is_available=True)
        products = all_products.count()

    context = {
        'all_products': all_products,
        'products': products
    }
    return render(request, 'storeapp/store_page.html', context=context)


class ProductDetailView(View):
    """
    Class Based View for Displaying the Product Detail
    """

    def get(self, request, category_slug, product_slug):
        """
        Response Against the incoming get request
        """
        print(category_slug, product_slug)
        try:
            product = Product.objects.filter(slug=product_slug)[0]
            print(product.get_url())
        except Exception as e:
            raise e

        context = {
            'single_product': product
        }
        return render(request, 'storeapp/product_detail.html',context=context)
