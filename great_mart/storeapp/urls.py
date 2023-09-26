from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreProductListView.as_view(), name='store-page'),
    path('category/<slug:slug>', views.get_product_by_category, name='get_product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('search/',views.SearchView.as_view(),name='search')
]
