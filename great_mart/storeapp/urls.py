from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreProductListView.as_view(), name='store-page'),
    path('<slug:slug>', views.get_product_by_category, name='get_product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.ProductDetailView.as_view(), name='product-detail')
]
