from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib import admin
from django.urls import path, include
from storeapp.views import (AllProductsListView, ProductDetailView)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', AllProductsListView.as_view(), name='home'),
                  # Store App Urls
                  path('store/', include('storeapp.urls')),
                  path('<slug:category_slug>/<slug:product_slug>', ProductDetailView.as_view(), name='product-detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
