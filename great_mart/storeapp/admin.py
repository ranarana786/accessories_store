from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'slug', 'stock',
                    'is_available', 'price', 'create_date',
                    'image', 'category']
    ordering = ['-create_date']
    prepopulated_fields = {
        'slug': ('prod_name',)
    }


admin.site.register(Product, ProductAdmin)
